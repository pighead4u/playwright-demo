# 试验区域设置
# 测试实验区域设置的增删改查
# 测试试验区域中的试验区工位的增删改查
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    print("test_area_test_search start")
    page = context.new_page()
    _test_search(page)
    page.close()
    print("test_area_test_search end")

    print("test_area_test_create start")
    page = context.new_page()
    _test_create(page)
    page.close()
    print("test_area_test_create end")

    print("test_area_test_update start")
    page = context.new_page()
    _test_update(page)
    page.close()
    print("test_area_test_update end")

    print("test_area_test_delete start")
    page = context.new_page()
    _test_delete(page)
    page.close()
    print("test_area_test_delete end")

    print("test_area_test_station_create start")
    page = context.new_page()
    _test_station_create(page)
    page.close()
    print("test_area_test_station_create end")

    print("test_area_test_station_update start")
    page = context.new_page()
    _test_station_update(page)
    page.close()
    print("test_area_test_station_update end")

    print("test_area_test_station_delete start")
    page = context.new_page()
    _test_station_delete(page)
    page.close()
    print("test_area_test_station_delete end")

    page.close()
    context.close()
    browser.close()

# 测试两种情况：
# 1、查询已经存在的试验区域
# 2、查询未存在试验区域
def _test_search(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "收发室")
    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/test_areas?name=%E6%94%B6%E5%8F%91%E5%AE%A4&code=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data']['list'][0]['name'] == '收发室',Exception("查询已存在的试验区域失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "收发室1")
    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/test_areas?name=%E6%94%B6%E5%8F%91%E5%AE%A41&code=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['code'] == 0,Exception("查询未存在的试验区域失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

# 测试两种情况：
# 1、创建已经存在的试验区域，创建失败
# 2、创建未存在的试验区域，创建成功
def _test_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click text=试验区名称试验区编码试验区类型请选择描述 >> [placeholder="请输入"]
    page.click("text=试验区名称试验区编码试验区类型请选择描述 >> [placeholder=\"请输入\"]")
    # Fill text=试验区名称试验区编码试验区类型请选择描述 >> [placeholder="请输入"]
    page.fill("text=试验区名称试验区编码试验区类型请选择描述 >> [placeholder=\"请输入\"]", "收发室")
    # Click text=试验区名称试验区编码试验区类型请选择描述 >> input[role="combobox"]
    page.click("text=试验区名称试验区编码试验区类型请选择描述 >> input[role=\"combobox\"]")
    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_areas") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1,Exception("不存在相同名称的试验区域")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click text=试验区名称试验区编码试验区类型请选择描述 >> [placeholder="请输入"]
    page.click("text=试验区名称试验区编码试验区类型请选择描述 >> [placeholder=\"请输入\"]")
    # Fill text=试验区名称试验区编码试验区类型请选择描述 >> [placeholder="请输入"]
    page.fill("text=试验区名称试验区编码试验区类型请选择描述 >> [placeholder=\"请输入\"]", "收发室1")
    # Click text=试验区名称试验区编码试验区类型请选择描述 >> input[role="combobox"]
    page.click("text=试验区名称试验区编码试验区类型请选择描述 >> input[role=\"combobox\"]")
    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")
    with page.expect_response("**/api/v1/test_areas") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "收发室1",Exception("创建新的试验区域失败！！！")

# 测试两种情况：
# 1、修改为已经存在的试验区域
# 2、修改为未存在的实验区域
def _test_update(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas")
    # Click text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")
    # Click text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.click("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]")
    # Fill text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.fill("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]", "仓库")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_areas/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1,Exception("修改后的试验区域已存在，测试用例失败！！！")
    # Click text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")
    # Click text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.click("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]")
    # Fill text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.fill("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]", "仓库1")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas"):
    with page.expect_response("**/api/v1/test_areas/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "仓库1",Exception("修改后的试验区域已存在，测试用例失败！！！")
    # page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(1) .ant-space div:nth-child(1) .text-button")
    # Click text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.click("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]")
    # Fill text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.fill("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]", "收发室")
    page.click("button:has-text(\"确定\")")

# 测试试验区域删除功能：
def _test_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "收发室1")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas"):
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/test_areas/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0,Exception("删除试验区域失败！！！")

# 测试两种情况：
# 1、创建已经存在的试验区工位，创建失败
# 2、创建未存在的试验区工位，创建成功
def _test_station_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "工位50")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_stations") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "工位50", Exception("创建新的试验区工位失败！！！")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "工位50")
    with page.expect_response("**/api/v1/test_stations") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("不存在相同名称的试验区工位！！！")

# 测试两种情况：
# 1、修改为已存在的试验区工位
# 2、修改为未存在的实验区工位
def _test_station_update(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations")
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(5) .ant-space div:nth-child(1) .text-button")
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "工位5")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_stations/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1,Exception("修改后的试验区工位已存在！！！")
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(5) .ant-space div:nth-child(1) .text-button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "工位40")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_stations/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "工位40", Exception("修改后的试验区工位已存在！！！")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(5) .ant-space div:nth-child(1) .text-button")
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "工位6")
    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations")

# 测试试验区工位删除功能：
def _test_station_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations")
    # Click a:has-text("3")
    page.click("a:has-text(\"3\")")
    # Click :nth-match(:text("删除"), 5)
    page.click(":nth-match(:text(\"删除\"), 5)")
    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/test_stations/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0,Exception("删除试验区工位失败！！！")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations")