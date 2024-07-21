from playwright.sync_api import Playwright, sync_playwright
from playwright.sync_api import Page, Browser
from dataclasses import dataclass
from typing import Optional

USER_AGENT      = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
URL_REPLIT_MAIN = 'https://replit.com/~'

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
        self.__new_user()

    def __init_playwright(self):
        self.playwright_instance = sync_playwright().start()
        self.browser    = self.playwright_instance.chromium.launch(headless=True)
        context         = self.browser.new_context(user_agent=USER_AGENT)   
        self.page       = context.new_page()      

    def __new_user(self):
        print("[i] Replit Data\n")
        user     = input("Enter Replit Username: ")
        password = input("Enter Replit Password: ")
        team     = input("Enter Replit Team: ")
        self.replit_user = User(user, password, team)

    def login(self):
        if not self.replit_user:
            raise ValueError("[!] User not initialized.")
        if not self.page:
            raise ValueError("[!] Page not initialized.")

        self.page.goto(URL_REPLIT_MAIN)
        self.page.fill('input[name="username"]', self.replit_user.username)
        self.page.wait_for_timeout(500)
        self.page.fill('input[name="password"]', self.replit_user.password)
        self.page.wait_for_timeout(500)
        self.page.click('button[data-cy="log-in-btn"]')
        self.page.wait_for_selector('h1:has-text("Home")')
        print("[i] Access\n")

    def js_selector(self, selector):
        if not self.page:
            raise ValueError("[!] Page not initialized.")
        result =  self.page.evaluate("""
            () => {
                return Array.from(document.querySelectorAll('%s'))
                    .map(element => element.textContent);
            }
        """ % selector)

        return result

    def guides_data(self):
        if not self.replit_user:
            raise ValueError("[!] User not initialized.")
        if not self.page:
            raise ValueError("[!] Page not initialized.")

        guides = {}
        self.page.goto(self.replit_user.team)
        self.page.wait_for_selector('span:has-text("Back to all Teams")')

        guides_content = self.page.query_selector_all('div.jsx-72ccb88e5e706d90.stack')
        
        for guide in guides_content:
            guides_title = guide.query_selector('h4.jsx-4210826056.heading.stack-heading')
            guides_title = guides_title.text_content() if guides_title else None

            tests = guide.query_selector_all('div.jsx-617b8fb557db5cc1 a.title-link')
            guide_content = {}
            for test in tests:
                test_title = test.query_selector('span') 
                test_link = test.get_attribute('href')

                test_title = test_title.text_content() if test_title else None
                guide_content.update({ test_title : test_link })

            guides.update({ guides_title : guide_content })

        return guides

    def close(self):
        if self.browser:
            self.browser.close()
            self.browser    = None
            self.page       = None

        if self.playwright_instance:
            self.playwright_instance.stop()

def main():
    replit = ReplitData()
    replit.init()

    replit.login()
    guides = replit.guides_data()
    print(guides)

    replit.close()


if __name__ == "__main__":
    main()

