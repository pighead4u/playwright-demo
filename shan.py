from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(2) .text-button")
    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings"):
    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/standard_bindings/25") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除绑定关系成功')
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)