from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    print("试验仪器查询：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "仪器2")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/instruments?name=%E4%BB%AA%E5%99%A82&code=&model=&manufacturer=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if (t['code'] == 0):
            print("暂无数据")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "仪器3")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/instruments?name=%E4%BB%AA%E5%99%A83&code=&model=&manufacturer=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if (t['data']['list'][0]['name'] =='仪器3'):
            print("查询试验仪器成功！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    print("实验仪器新增：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=仪器名称仪器类型请选择工位请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.click("text=仪器名称仪器类型请选择工位请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]")

    # Fill text=仪器名称仪器类型请选择工位请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.fill("text=仪器名称仪器类型请选择工位请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]", "仪器3")

    # Click .ant-form-item-control-input-content .ant-select .ant-select-selector
    page.click(".ant-form-item-control-input-content .ant-select .ant-select-selector")

    # Click text=EMC试验系统
    page.click("text=EMC试验系统")

    # Click text=工位请选择 >> svg
    page.click("text=工位请选择 >> svg")

    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span")

    # Click ul[role="group"] >> text=工位2
    page.click("ul[role=\"group\"] >> text=工位2")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instruments") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['code'] == -1):
            print("已存在相同名称的仪器")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=仪器名称仪器类型请选择工位请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.click("text=仪器名称仪器类型请选择工位请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]")

    # Fill text=仪器名称仪器类型请选择工位请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.fill("text=仪器名称仪器类型请选择工位请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]", "仪器100")

    # Click .ant-form-item-control-input-content .ant-select .ant-select-selector
    page.click(".ant-form-item-control-input-content .ant-select .ant-select-selector")

    # Click text=EMC试验系统
    page.click("text=EMC试验系统")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span")

    # Click text=工位2工位3工位4工位5工位6工位7工位8工位9工位10工位11工位12工位13工位14工位15工位16工位17工位18工位19工位20工位21工位22
    page.click("text=工位2工位3工位4工位5工位6工位7工位8工位9工位10工位11工位12工位13工位14工位15工位16工位17工位18工位19工位20工位21工位22")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instruments") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['data']['name'] == "仪器100"):
            print("新增试验仪器成功")

    print("试验仪器编辑：")
    page.click("td:nth-child(2) .ant-space div .text-button")

    # Click text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.click(
        "text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]")

    # Fill text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.fill(
        "text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]",
        "仪器1")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instruments/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的仪器')

    # Click td:nth-child(2) .ant-space div .text-button
    page.click("td:nth-child(2) .ant-space div .text-button")

    # Click text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.click(
        "text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]")

    # Fill text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.fill(
        "text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]",
        "仪器名称1")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments"):
    with page.expect_response("**/api/v1/instruments/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['name'] == "仪器名称1"):
            print('编辑试验仪器成功！')

    page.click("td:nth-child(2) .ant-space div .text-button")

    # Click text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.click(
        "text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]")

    # Fill text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.fill(
        "text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]",
        "仪器名称")

    page.click("button:has-text(\"确定\")")

    print("试验仪器删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "仪器100")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")

    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/instruments/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除仪器成功')

   # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments")

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

    print("删除仪器维修记录：")
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

    print("仪器周期新增：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records")

    # Click text=仪器周期检定表
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/inspect-records"):
    with page.expect_navigation():
        page.click("text=仪器周期检定表")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "检验单位1")

    # Click :nth-match([placeholder="请输入"], 2)
    page.click(":nth-match([placeholder=\"请输入\"], 2)")

    # Fill :nth-match([placeholder="请输入"], 2)
    page.fill(":nth-match([placeholder=\"请输入\"], 2)", "钱某某")

    # Click [placeholder="请选择"]
    page.click("[placeholder=\"请选择\"]")

    # Click .ant-calendar-current-week td:nth-child(2) .ant-calendar-date
    page.click(".ant-calendar-current-week td:nth-child(2) .ant-calendar-date")

    # Click :nth-match([placeholder="请选择"], 2)
    page.click(":nth-match([placeholder=\"请选择\"], 2)")

    # Click table[role="grid"] >> text=12
    page.click("table[role=\"grid\"] >> text=12")

    with page.expect_response("**/api/v1/inspect_records") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['data']['inspect_company'] == "检验单位1"):
            print("新增仪器检定成功！！！")

    print("仪器检定编辑：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/inspect-records")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "检验单位1111")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/inspect_records/11") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['inspect_company'] == "检验单位1111"):
            print('编辑成功！！！')

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "检验单位1")

    page.click("button:has-text(\"确定\")")

    print("仪器周期删除：")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(5) .ant-space div:nth-child(2) .text-button")
    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/inspect-records"):
    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/inspect_records/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除检验记录成功！！！')
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)