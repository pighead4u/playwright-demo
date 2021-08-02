from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    print("试验方案查询：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "试验方案8")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/test_plans?name=%E8%AF%95%E9%AA%8C%E6%96%B9%E6%A1%888") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        # print(t['data']['list'][0]['name'])
        if (t['data']['list'][0]['name']== '试验方案8'):
           print('查询成功')

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "实验方案8")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/test_plans?name=%E5%AE%9E%E9%AA%8C%E6%96%B9%E6%A1%888") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if (t['code'] == 0):
            print('暂无数据')

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans


    print("试验方案新增：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=试验方案名称试验方案编码设备种类(单选)请选择描述 >> [placeholder="请输入"]
    page.click("text=试验方案名称试验方案编码设备种类(单选)请选择描述 >> [placeholder=\"请输入\"]")

    # Fill text=试验方案名称试验方案编码设备种类(单选)请选择描述 >> [placeholder="请输入"]
    page.fill("text=试验方案名称试验方案编码设备种类(单选)请选择描述 >> [placeholder=\"请输入\"]", "试验方案11")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click text=变压器JP柜低压开关柜电缆分接箱断路器隔离开关环网柜高压开关柜配电线路故障指示器配电自动化终端箱变柱上开关一二次融合断路器 >> span
    page.click("text=变压器JP柜低压开关柜电缆分接箱断路器隔离开关环网柜高压开关柜配电线路故障指示器配电自动化终端箱变柱上开关一二次融合断路器 >> span")

    # Click ul[role="group"] >> text=油浸式变压器
    page.click("ul[role=\"group\"] >> text=油浸式变压器")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_plans") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['data']['name'] == "试验方案11"):
            print("新增试验方案成功")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=试验方案名称试验方案编码设备种类(单选)请选择描述 >> [placeholder="请输入"]
    page.click("text=试验方案名称试验方案编码设备种类(单选)请选择描述 >> [placeholder=\"请输入\"]")

    # Fill text=试验方案名称试验方案编码设备种类(单选)请选择描述 >> [placeholder="请输入"]
    page.fill("text=试验方案名称试验方案编码设备种类(单选)请选择描述 >> [placeholder=\"请输入\"]", "试验方案11")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click text=变压器JP柜低压开关柜电缆分接箱断路器隔离开关环网柜高压开关柜配电线路故障指示器配电自动化终端箱变柱上开关一二次融合断路器 >> span
    page.click("text=变压器JP柜低压开关柜电缆分接箱断路器隔离开关环网柜高压开关柜配电线路故障指示器配电自动化终端箱变柱上开关一二次融合断路器 >> span")

    # Click ul[role="group"] >> text=油浸式变压器
    page.click("ul[role=\"group\"] >> text=油浸式变压器")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_plans") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['code'] == -1):
            print("已存在相同名称的试验方案")




    print("试验方案编辑：")

    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")

    # Click text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.click("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]")

    # Fill text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.fill("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]", "试验方案8")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_plans/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的试验方案')

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")

    # Click text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.click("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]")

    # Fill text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.fill("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]", "试验方案40")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans"):
    with page.expect_response("**/api/v1/test_plans/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['name'] == "试验方案40"):
            print('编辑试验方案成功！')

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")

    # Click text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.click("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]")

    # Fill text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.fill("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]", "试验方案4")

    page.click("button:has-text(\"确定\")")

    print("试验方案删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "试验方案11")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans"):
    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/test_plans/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除试验方案成功')
    # Close page

    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)