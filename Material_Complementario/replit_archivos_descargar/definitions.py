import os
from playwright.sync_api import ElementHandle, Playwright, sync_playwright, Error as PlaywrightError
from playwright.sync_api import Page, Browser
from dataclasses import dataclass
from typing import Optional, List

USER_AGENT      = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
URL_REPLIT_MAIN = 'https://replit.com'

@dataclass
class Test:
    title   :   str
    link    :   str
    def __init__(self, title: Optional[str], link: Optional[str]):
        self.title  = title if title else "UNKNOW_TEST_TITLE"
        self.link   = link  if link  else "UNKNOW_TEST_TITLE_LINK"

@dataclass
class Guide:
    title   :   str
    tests    :   List[Test]
    def __init__(self, title: Optional[str], tests: List[Test]):
        self.title  = title if title else "UNKNOW_GUIDE_TITLE"
        self.tests   = tests

@dataclass
class User:
    username    : str
    password    : str
    team        : str

class ReplitData:
    def __init__(self):
        self.playwright_instance    : Optional[Playwright]  = None
        self.browser                : Optional[Browser]     = None
        self.page                   : Optional[Page]        = None
        self.replit_user            : Optional[User]        = None

    def init(self):
        self.__init_playwright()
        self.__init_user()

    def __init_playwright(self):
        try:
            self.playwright_instance = sync_playwright().start()
            self.browser    = self.playwright_instance.chromium.launch(headless=False)
            context         = self.browser.new_context(user_agent=USER_AGENT)   
            self.page       = context.new_page()      
        except Exception as err:
            raise Exception(f"[!] Failed on init playwright {err}")

    def __init_user(self):
        print("[i] Replit Data\n")
        user     = input("Enter Replit Username: ")
        password = input("Enter Replit Password: ")
        team     = input("Enter Replit Team (https://replit.com/team/{team_name}): ")
        self.replit_user = User(user, password, team)

    def login(self) -> Optional[Exception]:
        if not self.replit_user:
            raise ValueError("[!] User not initialized")
        if not self.page:
            raise ValueError("[!] Page not initialized")

        try:
            self.page.goto(f'{URL_REPLIT_MAIN}/~')
            self.page.fill('input[name="username"]', self.replit_user.username)
            self.page.wait_for_timeout(500)
            self.page.fill('input[name="password"]', self.replit_user.password)
            self.page.wait_for_timeout(500)
            self.page.click('button[data-cy="log-in-btn"]')
            self.page.wait_for_selector('h1:has-text("Home")')
        except Exception as err:
            return err

    def js_selector(self, selector: str) -> Optional[List[ElementHandle]]:
        if not self.page:
            raise ValueError("[!] Page not initialized")
        result: Optional[List[ElementHandle]] =  self.page.evaluate("""
            () => {
                return Array.from(document.querySelectorAll('%s'))
                    .map(element => element.textContent || "");
            }
        """ % selector)

        return result

    def guides_data(self) -> List[Guide]:
        if not self.replit_user:
            raise ValueError("[!] User not initialized")
        if not self.page:
            raise ValueError("[!] Page not initialized")

        try:
            replit_team = f"{URL_REPLIT_MAIN}/team/{self.replit_user.team}"

            self.page.goto(replit_team)
            self.page.wait_for_selector('span:has-text("Back to all Teams")')

            guide_elems = self.page.query_selector_all('div.jsx-72ccb88e5e706d90.stack')
            
            guides : List[Guide] = []

            def extract_test(test_elem: ElementHandle) -> Test:
                test_title  = test_elem.query_selector('span')                  
                test_link   = test_elem.get_attribute('href')                   
                                                                                
                test_title  = test_title.text_content() if test_title else None 
                return Test(test_title, test_link)

            def extract_guide(guide_elem: ElementHandle) -> Guide:
                guides_title    = guide_elem.query_selector('h4.jsx-4210826056.heading.stack-heading')
                guides_title    = guides_title.text_content() if guides_title else None

                tests_elems     = guide_elem.query_selector_all('div.jsx-617b8fb557db5cc1 a.title-link')
                tests           = [ extract_test(test_elem) for test_elem in tests_elems ]
                return Guide(guides_title, tests)

            guides = [ extract_guide(guide_elem) for guide_elem in guide_elems ]

            return guides

        except Exception as err:
            raise Exception(f"[!] Failed on extract guides data: {err}")

    def get_guides(self, guides: List[Guide]):
        if not self.replit_user:
            raise ValueError("[!] Failed on download_guides: Page not initialized")
        if not self.page:
            raise ValueError("[!] Failed on download_guides: Page not initialized")

        team_name = self.replit_user.team

        def create_dir(name_dir: str):
            try:
                os.makedirs(name=name_dir, exist_ok=True)
            except Exception as err:
                raise Exception(f"[!] Failed on create directories: {err}")

        def download_test(test: Test, page: Page = self.page, name_dir: str = '.'):
            print("\n[i] Downloading Test")
            with page.expect_download() as download_data:
                try:
                    page.goto(f"{URL_REPLIT_MAIN}/{test.link}.zip")
                except PlaywrightError as err:
                    if 'waiting until "load"' in err.args:
                        print(f"[!] Failed to Download {test.link}\n\t{err}")

            test_file       = download_data.value
            test_path_file  = os.path.join(name_dir, f"{test.title}.zip") 

            try:
                test_file.save_as(test_path_file)
                print(test_path_file)
            except PlaywrightError as err:
                print(f"[!] Failed to save the file {test.link}\n\t{err}")

        for guide in guides:
            for test_obj in guide.tests:
                team_name       = team_name.replace('/', '_')
                guide.title     = guide.title.replace('/', '_')
                test_obj.title  = test_obj.title.replace('/', '_')

                test_file_path = os.path.join(team_name, guide.title, test_obj.title)

                create_dir(test_file_path)
                download_test(test=test_obj, name_dir=test_file_path)

    def close(self):
        try:
            if self.browser:
                self.browser.close()
                self.browser    = None
                self.page       = None

            if self.playwright_instance:
                self.playwright_instance.stop()

        except Exception as err:
            raise Exception(f"[!] Failed on close the Replit instance: {err}")
