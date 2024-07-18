from playwright.sync_api import sync_playwright

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
URL = 'https://replit.com/~'

def js_selector(page, selector):
    result =  page.evaluate("""
        () => {
            return Array.from(document.querySelectorAll('%s'))
                .map(element => element.textContent);
        }
    """ % selector)

    return result


def replit_data():
    print("[i] Replit Data\n")
    replit_team     = input("Enter Replit Team: ")
    replit_user     = input("Enter Replit Username: ")
    replit_password = input("Enter Replit Password: ")

    return {'team': replit_team, 'user': replit_user, 'password': replit_password}

def login_page(page, url, **credentials):
    page.goto(url)
    page.fill('input[name="username"]', credentials['user'])
    page.wait_for_timeout(500)
    page.fill('input[name="password"]', credentials['password'])
    page.wait_for_timeout(500)
    page.click('button[data-cy="log-in-btn"]')
    page.wait_for_selector('h1:has-text("Home")')
    print("[i] Access\n")

    return page

def guides_data(page, team):
    guides = {}

    page.goto(team)
    page.wait_for_selector('span:has-text("Back to all Teams")')

    guides_content = page.query_selector_all('div.jsx-72ccb88e5e706d90.stack')
    
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


def main():
    replit = replit_data()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent=USER_AGENT)
        page = context.new_page()

        page = login_page(
            page    = page,
            url     = URL,
            user    =replit['user'],
            password=replit['password']
        )

        guides_replit = guides_data(page, replit['team'])
        print(guides_replit)

        browser.close()


if __name__ == "__main__":
    main()

