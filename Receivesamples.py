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

    print("收样新增：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive")

    # Click button:has-text("收样")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive/new"):
    with page.expect_navigation():
        page.click("button:has-text(\"收样\")")

    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive/new")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "123456789")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click li:nth-child(2) .ant-select-tree-switcher
    page.click("li:nth-child(2) .ant-select-tree-switcher")

    # Click ul[role="group"] >> text=JP柜
    page.click("ul[role=\"group\"] >> text=JP柜")

    # Click div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.click("div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input")

    # Fill div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.fill("div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input", "987654321")

    # Click div:nth-child(4) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.click("div:nth-child(4) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input")

    # Fill div:nth-child(4) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.fill("div:nth-child(4) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input", "设备1")

    # Click div:nth-child(5) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.click("div:nth-child(5) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input")

    # Fill div:nth-child(5) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.fill("div:nth-child(5) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input", "大")

    # Click input[role="combobox"]
    page.click("input[role=\"combobox\"]")

    # Click text=222
    page.click("text=222")

    # Click text=试验类型请选择 >> input[role="combobox"]
    page.click("text=试验类型请选择 >> input[role=\"combobox\"]")

    # Click text=自主送检
    page.click("text=自主送检")

    # Click [placeholder="请选择"]
    page.click("[placeholder=\"请选择\"]")

    # Click text=10
    page.click("text=10")

    page.click("div:nth-child(10) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input")

    page.fill("div:nth-child(10) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input", "1")

    # Click text=生产厂家请选择 >> input[role="combobox"]
    page.click("text=生产厂家请选择 >> input[role=\"combobox\"]")

    # Click text=开关公司
    page.click("text=开关公司")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click input[role="combobox"]
    page.click("input[role=\"combobox\"]")

    # Click text=单位1
    page.click("text=单位1")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "2")

    # Press Tab
    page.press("[placeholder=\"请输入\"]", "Tab")

    # Fill #rated_voltage
    page.fill("#rated_voltage", "2")

    # Press Tab
    page.press("#rated_voltage", "Tab")

    # Fill #rated_current
    page.fill("#rated_current", "2")

    # Press Tab
    page.press("#rated_current", "Tab")

    # Fill #rated_frequency
    page.fill("#rated_frequency", "2")

    # Press Tab
    page.press("#rated_frequency", "Tab")

    # Fill #jpg_wgbcrl
    page.fill("#jpg_wgbcrl", "2")

    # Press Tab
    page.press("#jpg_wgbcrl", "Tab")

    # Fill input[type="text"]
    page.fill("input[type=\"text\"]", "2")

    # Press Tab
    page.press("input[type=\"text\"]", "Tab")

    # Fill #rated_jy_voltage
    page.fill("#rated_jy_voltage", "2")

    # Press Tab
    page.press("#rated_jy_voltage", "Tab")

    # Fill #rated_dsns_current
    page.fill("#rated_dsns_current", "2")

    # Click button:has-text("完成")
    with page.expect_response("**/api/v1/devices") as response_info:
        page.click("button:has-text(\"完成\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['data']['name'] == "设备1"):
            print("新增设备成功！！！")

    with page.expect_navigation():
        page.click("button:has-text(\"返回收样列表\")")

    with page.expect_navigation():
        page.click("button:has-text(\"收样\")")

    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive/new")

        # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "123456789")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click li:nth-child(2) .ant-select-tree-switcher
    page.click("li:nth-child(2) .ant-select-tree-switcher")

    # Click ul[role="group"] >> text=JP柜
    page.click("ul[role=\"group\"] >> text=JP柜")

    # Click div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.click(
        "div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input")

    # Fill div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.fill(
        "div:nth-child(3) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input",
        "987654321")

    # Click div:nth-child(4) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.click(
        "div:nth-child(4) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input")

    # Fill div:nth-child(4) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.fill(
        "div:nth-child(4) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input",
        "设备1")

    # Click div:nth-child(5) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.click(
        "div:nth-child(5) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input")

    # Fill div:nth-child(5) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.fill(
        "div:nth-child(5) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input",
        "大")

    # Click input[role="combobox"]
    page.click("input[role=\"combobox\"]")

    # Click text=222
    page.click("text=222")

    # Click text=试验类型请选择 >> input[role="combobox"]
    page.click("text=试验类型请选择 >> input[role=\"combobox\"]")

    # Click text=自主送检
    page.click("text=自主送检")

    # Click [placeholder="请选择"]
    page.click("[placeholder=\"请选择\"]")

    # Click text=10
    page.click("text=10")

    # Click div:nth-child(10) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.click(
        "div:nth-child(10) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input")

    # Fill div:nth-child(10) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input
    page.fill(
        "div:nth-child(10) .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-input",
        "1")

    # Click text=生产厂家请选择 >> input[role="combobox"]
    page.click("text=生产厂家请选择 >> input[role=\"combobox\"]")

    # Click text=开关公司
    page.click("text=开关公司")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click input[role="combobox"]
    page.click("input[role=\"combobox\"]")

    # Click text=单位1
    page.click("text=单位1")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "2")

    # Press Tab
    page.press("[placeholder=\"请输入\"]", "Tab")

    # Fill #rated_voltage
    page.fill("#rated_voltage", "2")

    # Press Tab
    page.press("#rated_voltage", "Tab")

    # Fill #rated_current
    page.fill("#rated_current", "2")

    # Press Tab
    page.press("#rated_current", "Tab")

    # Fill #rated_frequency
    page.fill("#rated_frequency", "2")

    # Press Tab
    page.press("#rated_frequency", "Tab")

    # Fill #jpg_wgbcrl
    page.fill("#jpg_wgbcrl", "2")

    # Press Tab
    page.press("#jpg_wgbcrl", "Tab")

    # Fill input[type="text"]
    page.fill("input[type=\"text\"]", "2")

    # Press Tab
    page.press("input[type=\"text\"]", "Tab")

    # Fill #rated_jy_voltage
    page.fill("#rated_jy_voltage", "2")

    # Press Tab
    page.press("#rated_jy_voltage", "Tab")

    # Fill #rated_dsns_current
    page.fill("#rated_dsns_current", "2")

    # Click button:has-text("完成")
    with page.expect_response("**/api/v1/devices") as response_info:
        page.click("button:has-text(\"完成\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['code'] == -1):
            print("已存在相同设备")

    print("收样编辑：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive")

    # Click a:has-text("2")
    page.click("a:has-text(\"2\")")

    # Click :nth-match(:text("设备1"), 2)
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive/48"):
    with page.expect_navigation():
        page.click(":nth-match(:text(\"设备1\"), 2)")

    # Click button:has-text("编辑")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive/48/edit"):
    with page.expect_navigation():
        page.click("button:has-text(\"编辑\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "123456789")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click button:has-text("完成")
    with page.expect_response("**/api/v1/devices/*") as response_info:
        page.click("button:has-text(\"完成\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同二维码的设备')

    # Click button:has-text("返回收样列表")
    page.click("button:has-text(\"返回收样列表\")")
    # assert page.url == "http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive"

    # Click a:has-text("2")
    page.click("a:has-text(\"2\")")

    # Click :nth-match(:text("设备1"), 2)
    page.click(":nth-match(:text(\"设备1\"), 2)")
    # assert page.url == "http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive/48"

    # Click button:has-text("编辑")
    page.click("button:has-text(\"编辑\")")
    # assert page.url == "http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive/48/edit"

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "1234567891011")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click button:has-text("完成")
    with page.expect_response("**/api/v1/devices/*") as response_info:
        page.click("button:has-text(\"完成\")")
        t = response_info.value.json()
        if (t['data']['name'] == "设备1" and t['data']['qrcode'] == '1234567891011'):
            print('编辑收样成功！！！')

    # Click button:has-text("返回收样列表")
    page.click("button:has-text(\"返回收样列表\")")
    # assert page.url == "http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive"

    # Click a:has-text("2")
    page.click("a:has-text(\"2\")")

    # Click :nth-match(:text("设备1"), 2)
    page.click(":nth-match(:text(\"设备1\"), 2)")
    # assert page.url == "http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive/48"

    # Click button:has-text("编辑")
    page.click("button:has-text(\"编辑\")")
    # assert page.url == "http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive/48/edit"

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "12345678")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click button:has-text("下一步")
    page.click("button:has-text(\"下一步\")")

    # Click button:has-text("完成")
    page.click("button:has-text(\"完成\")")

    with page.expect_navigation():
        page.click("button:has-text(\"返回收样列表\")")

    print("收样删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "设备1")

    # Click #qrcode
    page.click("#qrcode")

    # Fill #qrcode
    page.fill("#qrcode", "123456789")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/devices/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除设备成功！！！')

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive")

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/devices/receive")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)