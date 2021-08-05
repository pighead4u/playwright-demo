# 试验仪器设置
# 测试试验仪器设置的增删改查
# 测试试验仪器设置中仪器维修记录的增删改查
# 测试试验仪器设置中仪器周期检定表的增删改查
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    print("test_instrument_test_search start")
    page = context.new_page()
    _test_search(page)
    page.close()
    print("test_instrument_test_search end")

    print("test_instrument_test_create start")
    page = context.new_page()
    _test_create(page)
    page.close()
    print("test_instrument_test_create end")

    print("test_instrument_test_update start")
    page = context.new_page()
    _test_update(page)
    page.close()
    print("test_instrument_test_update end")

    print("test_instrument_test_delete start")
    page = context.new_page()
    _test_delete(page)
    page.close()
    print("test_instrument_test_delete end")

    print("test_instrument_instrument_maintenance_create start")
    page = context.new_page()
    _instrument_maintenance_create(page)
    page.close()
    print("test_instrument_instrument_maintenance_create end")

    print("test_instrument_instrument_maintenance_update start")
    page = context.new_page()
    _instrument_maintenance_update(page)
    page.close()
    print("test_instrument_instrument_maintenance_update end")

    print("test_instrument_instrument_maintenance_delete start")
    page = context.new_page()
    _instrument_maintenance_delete(page)
    page.close()
    print("test_instrument_instrument_maintenance_delete end")

    print("test_instrument_instrument_cycle_create start")
    page = context.new_page()
    _instrument_cycle_create(page)
    page.close()
    print("test_instrument_instrument_cycle_create end")

    print("test_instrument_instrument_cycle_update start")
    page = context.new_page()
    _instrument_cycle_update(page)
    page.close()
    print("test_instrument_instrument_cycle_update end")

    print("test_instrument_instrument_cycle_delete start")
    page = context.new_page()
    _instrument_cycle_delete(page)
    page.close()
    print("test_instrument_instrument_cycle_delete end")

    page.close()
    context.close()
    browser.close()


# 测试两种情况：
# 1、查询已存在的试验仪器设置
# 2、查询未存在的试验仪器设置
def _test_search(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "仪器2")
    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/instruments?name=%E4%BB%AA%E5%99%A82&code=&model=&manufacturer=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['code'] == 0,Exception("查询未存在的试验仪器设置失败！！！")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "仪器3")
    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/instruments?name=%E4%BB%AA%E5%99%A83&code=&model=&manufacturer=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data']['list'][0]['name'] =='仪器3',Exception("查询已存在的试验仪器设置失败！！！")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

# 测试两种情况：
# 1、创建已存在的试验仪器，创建失败
# 2、创建未存在的试验仪器，创建成功
def _test_create(page):
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
        assert t['code'] == -1,Exception("不存在相同名称的试验仪器设置！！！")
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
        assert t['data']['name'] == "仪器100",Exception("创建新的试验仪器失败！！！")

# 测试两种情况：
# 1、修改为已存在的试验仪器标准
# 2、修改为未存在的试验仪器标准
def _test_update(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments")
    page.click("td:nth-child(2) .ant-space div .text-button")
    # Click text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.click( "text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]")
    # Fill text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.fill("text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]","仪器1")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instruments/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1,Exception("修改后的试验仪器已存在，测试用例失败！！！")

    # Click td:nth-child(2) .ant-space div .text-button
    page.click("td:nth-child(2) .ant-space div .text-button")
    # Click text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.click("text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]")
    # Fill text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.fill("text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]", "仪器名称1")
    with page.expect_response("**/api/v1/instruments/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "仪器名称1",Exception("修改后的试验仪器已存在，测试用例失败！！！")
    page.click("td:nth-child(2) .ant-space div .text-button")
    # Click text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.click("text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]")
    # Fill text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder="请输入"]
    page.fill("text=仪器名称仪器类型线路组温升试验系统（60kva）-1工位工位10请选择仪器编码仪器型号生产厂家出厂编号IP地址端口号购买时间在报告中显示不显示显示准确级备注 >> [placeholder=\"请输入\"]","仪器名称")
    page.click("button:has-text(\"确定\")")

# 测试删除功能是否成功
def _test_delete(page):
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
        assert t['code'] == 0,Exception("删除试验仪器失败！！！")


   # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments")

#测试仪器维修新增功能是否成功
def _instrument_maintenance_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records")
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
        assert t['data']['maintenance_user'] == "钱某某",Exception("创建新的仪器维修记录失败")

# 测试仪器维修编辑功能是否成功
def _instrument_maintenance_update(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "孙某某")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records"):
    with page.expect_response("**/api/v1/maintenance_records/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['maintenance_user'] == "孙某某",Exception("修改仪器维修记录失败！！！")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "王某某")
    page.click("button:has-text(\"确定\")")

# 测试仪器维修删除功能是否成功
def _instrument_maintenance_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records")
    # Click a:has-text("2")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(10) .ant-space div:nth-child(2) .text-button")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/maintenance_records/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0,Exception("删除维修记录失败！！！")

def _instrument_cycle_create(page):
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/inspect-records")
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
        assert t['data']['inspect_company'] == "检验单位1",Exception("创建新的仪器周期表失败！！！")

def _instrument_cycle_update(page):
        # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/maintenance-records
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/inspect-records")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "检验单位1111")
    with page.expect_response("**/api/v1/inspect_records/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['inspect_company'] == "检验单位1111", Exception("修改仪器周期检定表失败！！！")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "检验单位1")
    page.click("button:has-text(\"确定\")")

def _instrument_cycle_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instruments/44/inspect-records")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(2) .text-button")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/inspect_records/*") as response_info:
        t = response_info.value.json()
        assert  t['code'] == 0,Exception("删除检验记录失败！！！")



