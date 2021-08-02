from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()


    print("新增仪器维修记录：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments")

    # Click text=1仪器名称2仪器13仪器34仪器45仪器56仪器67仪器78仪器89仪器910仪器10 >> button
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records"):
    with page.expect_navigation():
        page.click("text=1仪器名称2仪器13仪器34仪器45仪器56仪器67仪器78仪器89仪器910仪器10 >> button")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "钱某某")

    # Click :nth-match([placeholder="请输入"], 2)
    page.click(":nth-match([placeholder=\"请输入\"], 2)")

    # Fill :nth-match([placeholder="请输入"], 2)
    page.fill(":nth-match([placeholder=\"请输入\"], 2)", "123")

    # Click [placeholder="请选择"]
    page.click("[placeholder=\"请选择\"]")

    # Click .ant-calendar-current-week td:nth-child(2) .ant-calendar-date
    page.click(".ant-calendar-current-week td:nth-child(2) .ant-calendar-date")

    # Click :nth-match([placeholder="请输入"], 3)
    page.click(":nth-match([placeholder=\"请输入\"], 3)")

    # Fill :nth-match([placeholder="请输入"], 3)
    page.fill(":nth-match([placeholder=\"请输入\"], 3)", "好")

    with page.expect_response("**/api/v1/maintenance_records") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['data']['maintenance_user'] == "钱某某"):
            print("新增仪器维修记录成功")

    print("编辑仪器维修记录：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "孙某某")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records"):
    with page.expect_response("**/api/v1/maintenance_records/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['maintenance_user'] == "孙某某"):
            print('编辑成功！')
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "王某某")
    page.click("button:has-text(\"确定\")")

    print("删除仪器维修记录")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records")

    # Click a:has-text("2")
    page.click("a:has-text(\"2\")")

    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")

    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/maintenance_records/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除维修记录成功！！！')

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)