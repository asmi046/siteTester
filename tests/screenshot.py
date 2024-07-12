import os

from playwright.async_api import async_playwright
from urllib.parse import urlparse
from datetime import datetime

def get_file_name(url):
    url_part = urlparse(url)
    cdt = datetime.now()
    return f"{url_part.hostname}_{cdt.date()}_{cdt.hour}_{cdt.minute}_{cdt.second}"

async def get_screenshot(url="http://playwright.dev"):
    async with async_playwright() as p:
        # os.makedirs('scrinshots', exist_ok=True)

        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        patch = f"scrinshots/{get_file_name(url)}.png"
        await page.screenshot(path=patch, full_page=True)
        return patch
