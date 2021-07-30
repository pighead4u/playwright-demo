from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    print("试验标准新增：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")

    # Click text=试验标准
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings"):
    with page.expect_navigation():
        page.click("text=试验标准")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=国家标准名称请选择 >> input[role="combobox"]
    page.click("text=国家标准名称请选择 >> input[role=\"combobox\"]")

    # Click text=国标1
    page.click("text=国标1")

    # Click text=国家标准类型请选择 >> input[role="combobox"]
    page.click("text=国家标准类型请选择 >> input[role=\"combobox\"]")

    # Click :nth-match(:text("检测依据"), 2)
    page.click(":nth-match(:text(\"检测依据\"), 2)")

    # Click text=设备种类请选择 >> input[role="combobox"]
    page.click("text=设备种类请选择 >> input[role=\"combobox\"]")

    # Click text=油浸式变压器
    page.click("text=油浸式变压器")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/standard_bindings?test_item_id=39") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['data']['list'][-1]['standard'] == "国标1"):
            print("新增成功")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=国家标准名称请选择 >> input[role="combobox"]
    page.click("text=国家标准名称请选择 >> input[role=\"combobox\"]")

    # Click :nth-match(:text("国标1"), 2)
    page.click(":nth-match(:text(\"国标1\"), 2)")

    # Click text=国家标准类型请选择 >> input[role="combobox"]
    page.click("text=国家标准类型请选择 >> input[role=\"combobox\"]")

    # Click :nth-match(:text("检测依据"), 3)
    page.click(":nth-match(:text(\"检测依据\"), 3)")

    # Click text=设备种类请选择 >> input[role="combobox"]
    page.click("text=设备种类请选择 >> input[role=\"combobox\"]")

    # Click :nth-match(:text("油浸式变压器"), 2)
    page.click(":nth-match(:text(\"油浸式变压器\"), 2)")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings"):
    with page.expect_response("**/api/v1/standard_bindings") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('绑定关系已存在')

    print("试验标准编辑：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")
    # Click span:has-text("国标1")
    page.click("span:has-text(\"国标1\")")

    # Click :nth-match(:text("国标2"), 2)
    page.click(":nth-match(:text(\"国标2\"), 2)")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/standard_bindings/22") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('修改后的绑定关系已存在')

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")
    # Click span:has-text("国标1")
    page.click("span:has-text(\"国标1\")")

    # Click text=国标3
    page.click("text=国标3")
    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings"):
    with page.expect_response("**/api/v1/standard_bindings/22") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['data']['standard'] == "国标3"):
            print('编辑成功')

    print("试验标准删除：")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)