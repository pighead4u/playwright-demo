from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    print("仪器类型新增：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instrument-types
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instrument-types")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "EMC")

    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "EMC试验系统")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instrument_types") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的仪器类型')

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "1234567")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instrument_types") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        # print(t['data']['id'])
        if (t['data']['name'] == '1234567'):
            print("新增成功")
    # ------------------------------------------------------------------------------------------------
    print("仪器类型重命名：")
    # Click text=1234567重命名删除 >> button
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instrument-types")

    page.click("text=1234567重命名删除 >> button")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "")

    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "EMC")

    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "EMC试验系统")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instrument_types") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的仪器类型')
    # Click text=1234567重命名删除 >> button
    page.click("text=1234567重命名删除 >> button")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "123456789")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instrument_types") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['data']['name'] == '123456789'):
            print('重命名成功')

    # Click text=123456789重命名删除 >> :nth-match(button, 2)
    page.click("text=123456789重命名删除 >> :nth-match(button, 2)")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instrument-types"):
    with page.expect_navigation():
        page.click("button:has-text(\"确定\")")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)