import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://rubexgroup.ru/")
    await page.get_by_role("link", name="Заказать звонок").click()
    await page.get_by_role("textbox", name="Ф.И.О").click()
    await page.get_by_role("textbox", name="Ф.И.О").fill("Тест Тестович")
    await page.get_by_role("textbox", name="Контактный телефон*").click()
    await page.get_by_role("textbox", name="Контактный телефон*").fill("3333333333")
    await page.get_by_placeholder("Контактный телефон*").click()
    await page.get_by_placeholder("e-mail*").click()
    await page.get_by_placeholder("e-mail*").fill("test@test.ru")
    # await page.locator("select[name=\"napravl\"]").select_option("Карьера")
    await page.get_by_role("button", name="Отправить").click()

    # ---------------------
    await context.close()
    await browser.close()


async def recall_test():
    async with async_playwright() as playwright:
        await run(playwright)