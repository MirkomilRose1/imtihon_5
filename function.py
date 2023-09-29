from playwright.sync_api import sync_playwright


def capture_first_post_screenshot():
    url = 'https://kun.uz/news/category/jahon'
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        screenshot = page.screenshot(path='first_post_screenshot.png')
        browser.close()

    return screenshot


capture_first_post_screenshot()
