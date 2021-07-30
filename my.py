from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://mes-dev.tunnel.shunjiantech.cn/
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/")

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/")

    # Click li[role="none"] div:has-text("试验信息管理")
    page.click("li[role=\"none\"] div:has-text(\"试验信息管理\")")

    # Click text=试验方案设置
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans"):
    with page.expect_navigation():
        page.click("text=试验方案设置")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "试验方案2")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")

    # Click text=电缆分接箱低压电缆分支箱高压电缆分支箱 >> div
    page.click("text=电缆分接箱低压电缆分支箱高压电缆分支箱 >> div")

    # Click text=低压电缆分支箱
    page.click("text=低压电缆分支箱")

    # Click text=高压电缆分支箱
    page.click("text=高压电缆分支箱")

    # Click text=低压开关柜低压开关柜 >> div
    page.click("text=低压开关柜低压开关柜 >> div")

    # Click [id="sub_menu_5_$$_65-popup"] >> text=低压开关柜
    page.click("[id=\"sub_menu_5_$$_65-popup\"] >> text=低压开关柜")

    # Click text=变压器油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器 >> div
    page.click("text=变压器油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器 >> div")

    # Click text=油浸式变压器
    page.click("text=油浸式变压器")

    # Click td:has-text("油浸变压器方案")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans/40/test-item-bindings"):
    with page.expect_navigation():
        page.click("td:has-text(\"油浸变压器方案\")")

    # Click a:has-text("试验方案设置")
    page.click("a:has-text(\"试验方案设置\")")
    # assert page.url == "http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans"

    # Click text=配电线路故障指示器电缆外施信号型就地故障指示器电缆外施信号型远传故障指示器电缆稳态特征型就地故障指示器电缆稳态特征型远传故障指示器架空外施信号型就地故障指示器架 >> div
    page.click("text=配电线路故障指示器电缆外施信号型就地故障指示器电缆外施信号型远传故障指示器电缆稳态特征型就地故障指示器电缆稳态特征型远传故障指示器架空外施信号型就地故障指示器架 >> div")

    # Click text=电缆外施信号型就地故障指示器
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans"):
    with page.expect_navigation():
        page.click("text=电缆外施信号型就地故障指示器")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
