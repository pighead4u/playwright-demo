from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")

    # Click text=判断标准
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings"):
    # with page.expect_navigation():
    #     page.click("text=判断标准")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=设备种类请选择 >> input[role="combobox"]
    page.click("text=设备种类请选择 >> input[role=\"combobox\"]")

    # Click :nth-match(:text("油浸式变压器"), 2)
    page.click(":nth-match(:text(\"油浸式变压器\"), 2)")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "111")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/criteria_bindings") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['device_category'])
        # print(t['data']['device_category_id'])
        if (t['data']['device_category'] == '油浸式变压器' and t['data']['device_category_id'] == 5):
            print("新增判断标准成功")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=设备种类请选择 >> input[role="combobox"]
    page.click("text=设备种类请选择 >> input[role=\"combobox\"]")

    # Click :nth-match(:text("油浸式变压器"), 3)
    page.click(":nth-match(:text(\"油浸式变压器\"), 3)")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "111")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings"):
    with page.expect_response("**/api/v1/criteria_bindings") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('绑定关系已存在')

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)