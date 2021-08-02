from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    print("收样查询：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "干式电力变压器")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/devices?name=%E5%B9%B2%E5%BC%8F%E7%94%B5%E5%8A%9B%E5%8F%98%E5%8E%8B%E5%99%A8") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if (t['data']['list'][0]['name'] == '干式电力变压器'):
            print('查询成功！！！')

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "干式电力变压器1")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/devices?name=%E5%B9%B2%E5%BC%8F%E7%94%B5%E5%8A%9B%E5%8F%98%E5%8E%8B%E5%99%A81") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if (t['code'] == 0):
            print('暂无数据')

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)