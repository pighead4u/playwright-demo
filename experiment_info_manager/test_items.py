# 试验项目设置
# 测试试验项目设置的增删改查
# 测试试验项目设置中的工位绑定增删改
# 测试试验项目设置中的试验标准增删改
# 测试试验项目设置中的判断标准增删改
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    print("测试试验项目设置")

    print("test_items_test_search start")
    page = context.new_page()
    _test_search(page)
    page.close()
    print("test_items_test_search end")

    print("test_items_test_create start")
    page = context.new_page()
    _test_create(page)
    page.close()
    print("test_items_test_create end")

    print("test_items_test_update start")
    page = context.new_page()
    _test_update(page)
    page.close()
    print("test_items_test_update end")

    print("test_items_test_delete start")
    page = context.new_page()
    _test_delete(page)
    page.close()
    print("test_items_test_delete end")

    print("测试试验项目设置中的工位绑定：")

    print("test_items_station_binding_create start")
    page = context.new_page()
    _station_binding_create(page)
    page.close()
    print("test_items_station_binding_create end")

    print("test_items_station_binding_update start")
    page = context.new_page()
    _station_binding_update(page)
    page.close()
    print("test_items_station_binding_update end")

    print("test_items_station_binding_delete start")
    page = context.new_page()
    _station_binding_delete(page)
    page.close()
    print("test_items_station_binding_delete end")

    print("测试试验项目设置中的试验判断：")

    print("test_items_test_judgment_create start")
    page = context.new_page()
    _test_judgment_create(page)
    page.close()
    print("test_items_test_judgment_create end")

    print("test_items_test_judgment_update start")
    page = context.new_page()
    _test_judgment_update(page)
    page.close()
    print("test_items_test_judgment_update end")

    print("test_items_test_judgment_delete start")
    page = context.new_page()
    _test_judgment_delete(page)
    page.close()
    print("test_items_test_judgment_delete end")

    print("测试试验项目设置中的判断标准：")

    print("test_items_judgment_criteria_create start")
    page = context.new_page()
    _judgment_criteria_create(page)
    page.close()
    print("test_items_judgment_criteria_create end")

    print("test_items_judgment_criteria_update start")
    page = context.new_page()
    _judgment_criteria_update(page)
    page.close()
    print("test_items_judgment_criteria_update end")

    print("test_items_judgment_criteria_delete start")
    page = context.new_page()
    _judgment_criteria_delete(page)
    page.close()
    print("test_items_judgment_criteria_delete end")

    page.close()
    context.close()
    browser.close()


# 测试两种情况：
# 1、查询已经存在的试验项目设置
# 2、查询未存在的试验项目设置
def _test_search(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "温升试验")
    with page.expect_response("**/api/v1/test_items?name=%E6%B8%A9%E5%8D%87%E8%AF%95%E9%AA%8C") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data']['total'] == 5, Exception("查询已存在的试验项目失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "温升试验1")
    with page.expect_response("**/api/v1/test_items?name=%E6%B8%A9%E5%8D%87%E8%AF%95%E9%AA%8C1") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data']['total'] == 0, Exception("查询未存在的试验项目失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")


# 测试两种情况：
# 1、创建已经存在的试验项目，创建失败
# 2、创建未存在的试验项目，创建成功
def _test_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码英文名称描述 >> [placeholder="请输入"]
    page.click("text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码英文名称描述 >> [placeholder=\"请输入\"]")
    # Fill text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码英文名称描述 >> [placeholder="请输入"]
    page.fill("text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码英文名称描述 >> [placeholder=\"请输入\"]", "111")
    # Click .ant-col.ant-col-12 .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector
    page.click(
        ".ant-col.ant-col-12 .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector")
    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")
    # Click div[role="combobox"] span:has-text("请选择")
    page.click("div[role=\"combobox\"] span:has-text(\"请选择\")")
    # Click li:nth-child(2) .ant-select-tree-switcher
    page.click("li:nth-child(2) .ant-select-tree-switcher")
    # Click ul[role="group"] >> text=JP柜
    page.click("ul[role=\"group\"] >> text=JP柜")
    # Click text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder="请输入"], 4)
    page.click("text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder=\"请输入\"], 4)")
    # Fill text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder="请输入"], 4)
    page.fill("text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder=\"请输入\"], 4)", "sdf")
    with page.expect_response("**/api/v1/test_items") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "111", Exception("创建新的试验项目失败！！！")
        assert t['data']['device_categories'][0]['name'] == "JP柜", Exception("创建新的试验项目失败！！！")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码英文名称描述 >> [placeholder="请输入"]
    page.click("text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码英文名称描述 >> [placeholder=\"请输入\"]")
    # Fill text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码英文名称描述 >> [placeholder="请输入"]
    page.fill("text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码英文名称描述 >> [placeholder=\"请输入\"]", "温升试验")
    # Click .ant-col.ant-col-12 .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector
    page.click(
        ".ant-col.ant-col-12 .ant-row .ant-col.ant-form-item-control .ant-form-item-control-input .ant-form-item-control-input-content .ant-select .ant-select-selector")
    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")
    # Click div[role="combobox"] span:has-text("请选择")
    page.click("div[role=\"combobox\"] span:has-text(\"请选择\")")
    # Click li:nth-child(2) .ant-select-tree-switcher
    page.click("li:nth-child(2) .ant-select-tree-switcher")
    # Click ul[role="group"] >> text=JP柜
    page.click("ul[role=\"group\"] >> text=JP柜")
    page.click("text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder=\"请输入\"], 4)")
    # Fill text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder="请输入"], 4)
    page.fill("text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder=\"请输入\"], 4)", "")
    # Press CapsLock
    page.press("text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder=\"请输入\"], 4)",
               "CapsLock")
    # Press CapsLock
    page.press("text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder=\"请输入\"], 4)",
               "CapsLock")
    # Fill text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder="请输入"], 4)
    page.fill("text=试验项目名称试验项目类型例行设备种类(多选)JP柜 请选择试验项目内容试验项目编码英文名称描述 >> :nth-match([placeholder=\"请输入\"], 4)", "t_wssy")
    with page.expect_response("**/api/v1/test_items") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("不存在相同名称的试验项目设置！！！")


# 测试两种情况：
# 1、修改为已经存在的试验项目
# 2、修改为未存在的试验项目
def _test_update(page):
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items")
    # Click text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")
    # Click text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.click("text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]")
    # Fill text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.fill("text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]",
        "温升试验（）")
    # Press ArrowLeft
    page.press("text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]",
        "ArrowLeft")
    # Fill text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.fill("text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]",
        "温升试验（干变）")
    with page.expect_response("**/api/v1/test_items/39") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("修改后的试验项目设置已存在，测试用例失败！！！")
    # Click text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")
    # Click text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.click("text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]")
    # Fill text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.fill("text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]",
        "温升试验1")
    with page.expect_response("**/api/v1/test_items/39") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "温升试验1", Exception("修改后的试验项目设置已存在，测试用例失败！！！")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(1) .ant-space div:nth-child(1) .text-button")
    # Click text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.click("text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]")
    # Fill text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.fill("text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]","温升试验")

    page.click("button:has-text(\"确定\")")


# 测试删除试验项目功能是否成功：
def _test_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "111")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items"):
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/test_items/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0, Exception("删除试验项目失败！！！")


# 测试两种情况：
# 1、创建已经存在的工位绑定，创建失败
# 2、创建未存在的工位绑定，创建成功
def _station_binding_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")
    # Click li:nth-child(5) .ant-select-tree-switcher
    page.click("li:nth-child(5) .ant-select-tree-switcher")
    # Click ul[role="group"] >> text=b3
    page.click("ul[role=\"group\"] >> text=b3")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_station_bindings") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("不存在相同的绑定关系！！！")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")
    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span")
    # Click text=工位2工位3工位4工位5工位6工位7工位8工位9工位10工位11工位12工位13工位14工位15工位16工位17工位18工位19工位20工位21工位22
    page.click("text=工位2工位3工位4工位5工位6工位7工位8工位9工位10工位11工位12工位13工位14工位15工位16工位17工位18工位19工位20工位21工位22")
    with page.expect_response("**/api/v1/test_station_bindings?test_item_id=39") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['list'][1]['test_area'] == "收发室", Exception("创建新的工位绑定设置失败!!!")


# 测试工位绑定删除功能是否成功
def _station_binding_delete(page):
    # Click :nth-match(:text("删除"), 5)
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(2) .text-button")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/test_station_bindings/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0, Exception("删除绑定关系失败！！！")


# 测试两种情况：
# 1、修改为已经存在的工位绑定
# 2、修改为未存在的工位绑定
def _station_binding_update(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")
    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区")
    # Click li:nth-child(6) .ant-select-tree-switcher
    page.click("li:nth-child(6) .ant-select-tree-switcher")
    # Click ul[role="group"] >> text=油化工位
    page.click("ul[role=\"group\"] >> text=油化工位")
    with page.expect_response("**/api/v1/test_station_bindings/51") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("修改后的绑定关系已存在，测试用例失败！！！")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")
    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span")
    # Click span:has-text("工位2")
    page.click("span:has-text(\"工位2\")")
    with page.expect_response("**/api/v1/test_station_bindings/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['test_station'] == "工位2", Exception("修改后的绑定关系已存在，测试用例失败！！！")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")
    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span")
    # Click span:has-text("工位2")
    page.click("span:has-text(\"工位3\")")
    page.click("button:has-text(\"确定\")")


# 测试两种情况：
# 1、创建已经存在的试验判断，创建失败
# 2、创建未存在的试验判断，创建成功
def _test_judgment_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings")
    page.click("button:has-text(\"新增\")")
    page.click("text=国家标准名称请选择 >> input[role=\"combobox\"]")
    page.click("text=国标1")
    page.click("text=国家标准类型请选择 >> input[role=\"combobox\"]")
    page.click(":nth-match(:text(\"检测依据\"), 3)")
    page.click("text=设备种类请选择 >> input[role=\"combobox\"]")
    page.click(":nth-match(:text(\"油浸式变压器\"), 2)")
    with page.expect_response("**/api/v1/standard_bindings?test_item_id=39") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['list'][-1]['standard'] == "国标1", Exception("创建新的试验判断失败!!!")
    page.click("button:has-text(\"新增\")")
    page.click("text=国家标准名称请选择 >> input[role=\"combobox\"]")
    page.click(":nth-match(:text(\"国标1\"), 2)")
    page.click("text=国家标准类型请选择 >> input[role=\"combobox\"]")
    page.click(":nth-match(:text(\"检测依据\"), 4)")
    page.click("text=设备种类请选择 >> input[role=\"combobox\"]")
    page.click(":nth-match(:text(\"油浸式变压器\"), 3)")
    with page.expect_response("**/api/v1/standard_bindings") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("不存在相同名称的试验判断！！！")


# 测试两种情况：
# 1、修改为已经存在的试验判断
# 2、修改为未存在的试验判断
def _test_judgment_update(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(1) .text-button")
    page.click("span:has-text(\"国标1\")")
    page.click(":nth-match(:text(\"国标2\"), 2)")
    with page.expect_response("**/api/v1/standard_bindings/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("修改后的试验判断已存在，测试用例失败！！！")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(1) .text-button")
    page.click("span:has-text(\"国标1\")")
    page.click("text=国标3")
    with page.expect_response("**/api/v1/standard_bindings/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['standard'] == "国标3", Exception("修改后的试验判断已存在，测试用例失败！！！")


# 测试试验判断删除功能是否成功
def _test_judgment_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(2) .text-button")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/standard_bindings/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0, Exception("删除绑定关系失败！！！")


# 测试两种情况：
# 1、创建已经存在的判断标准，创建失败
# 2、创建未存在的判断标准，创建成功
def _judgment_criteria_create(page):
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
        assert t['data']['device_category'] == '油浸式变压器', Exception("创建新的判断标准失败!!!")
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
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings"):
    with page.expect_response("**/api/v1/criteria_bindings") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("不存在相同名称的判断标准！！！")


# 测试两种情况：
# 1、修改为已经存在的判断标准
# 2、修改为未存在的判断标准
def _judgment_criteria_update(page):
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(1) .text-button")
    # Click span:has-text("油浸式变压器")
    page.click("span:has-text(\"油浸式变压器\")")
    # Click :nth-match(:text("非晶合金油浸式变压器"), 2)
    page.click(":nth-match(:text(\"非晶合金油浸式变压器\"), 2)")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/criteria_bindings/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("修改后的判断标准已存在，测试用例失败！！！")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(1) .text-button")
    # Click span:has-text("油浸式变压器")
    page.click("span:has-text(\"油浸式变压器\")")
    # Click .rc-virtual-list-holder-inner div:nth-child(4)
    page.click(".rc-virtual-list-holder-inner div:nth-child(4)")
    with page.expect_response("**/api/v1/criteria_bindings/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['device_category'] == "有载调压变压器", Exception("修改后的判断标准已存在，测试用例失败！！！")


# 测试判断标准删除功能是否成功
def _judgment_criteria_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(2) .text-button")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/criteria_bindings/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0, Exception("删除判断标准失败！！！")
