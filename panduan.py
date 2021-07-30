from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    print("判断标准新增:")

    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")


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

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings


    print("判断标准编辑：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")
    # Click span:has-text("油浸式变压器")
    page.click("span:has-text(\"油浸式变压器\")")

    # Click :nth-match(:text("非晶合金油浸式变压器"), 2)
    page.click(":nth-match(:text(\"非晶合金油浸式变压器\"), 2)")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/criteria_bindings/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1) and t['message'] == '修改后的绑定关系已存在':
            print('已存在相同名称的企业')

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button
    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click span:has-text("油浸式变压器")
    page.click("span:has-text(\"油浸式变压器\")")

    # Click text=箱变（干式）
    page.click("text=箱变（干式）")


    with page.expect_response("**/api/v1/criteria_bindings/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['device_category'] == '箱变（干式）' and t['data']['device_category_id'] == 116):
            print('编辑判断标准成功！')

    print("判断标准删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")


    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(2) .text-button")


    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/criteria_bindings/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除判断标准成功')

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)