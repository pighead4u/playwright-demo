from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    print("查询：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "温升试验")

    with page.expect_response("**/api/v1/test_items?name=%E6%B8%A9%E5%8D%87%E8%AF%95%E9%AA%8C") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        # print(t['data']['list'][0]['name'])
        # print(t['data']['total'])
        if (t['data']['total'] == 5):
            print("查询成功")
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
        # print(t)
        # print(t['data']['total'])
        if (t['data']['total'] == 0):
            print("暂无数据")

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click .ant-select-selector
    page.click(".ant-select-selector")

    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")

    with page.expect_response("**/api/v1/test_items?name=&test_item_type_id=10") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        # print(t)
        # print(t['data']['total'])
        if (t['data']['total'] == 49):
            print("查询成功")

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    print("新增:")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码描述 >> [placeholder="请输入"]
    page.click("text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码描述 >> [placeholder=\"请输入\"]")

    # Fill text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码描述 >> [placeholder="请输入"]
    page.fill("text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码描述 >> [placeholder=\"请输入\"]", "111")

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

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_items") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        print(t['data']['name'])
        print(t['data']['device_categories'][0]['name'])
        if (t['data']['name'] == "111" and t['data']['device_categories'][0]['name'] == "JP柜"):
            print('新增试验项目成功')

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    page.click("text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码描述 >> [placeholder=\"请输入\"]")

    # Fill text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码描述 >> [placeholder="请输入"]
    page.fill("text=试验项目名称试验项目类型请选择设备种类(多选) 请选择试验项目内容试验项目编码描述 >> [placeholder=\"请输入\"]", "温升试验")

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

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items"):
    with page.expect_response("**/api/v1/test_items") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的试验项目')

    print("编辑：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items")

    # Click text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")

    # Click text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.click(
        "text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]")

    # Fill text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.fill(
        "text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]",
        "温升试验（）")

    # Press ArrowLeft
    page.press(
        "text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]",
        "ArrowLeft")

    # Fill text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.fill(
        "text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]",
        "温升试验（干变）")

    with page.expect_response("**/api/v1/test_items/39") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的试验项目')

    # Click text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")

    # Click text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.click(
        "text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]")

    # Fill text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder="请输入"]
    page.fill(
        "text=试验项目名称试验项目类型型式设备种类(多选)油浸式变压器非晶合金油浸式变压器干式配电变压器有载调压变压器箱变（干式）电缆外施信号型就地故障指示器DTU二遥标准型 >> [placeholder=\"请输入\"]",
        "温升试验1")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items"):
    with page.expect_response("**/api/v1/test_items/39") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['name'] == "温升试验1"):
            print('编辑成功！')

    print("删除：")


    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items")
#----------------------------------------------------------------------------------------------------------------------
    print("工位绑定新增：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items

    # Click text=1温升试验2温升试验（干变）3温升试验（一二次融合）4绕组对地及绕组间直流绝缘电阻测量5绕组介质损耗因素测量（tanδ）、绕组对地及绕组间的电容量测量6绕组电阻 >> button
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings"):
    with page.expect_navigation():
        page.click("text=1温升试验2温升试验（干变）3温升试验（一二次融合）4绕组对地及绕组间直流绝缘电阻测量5绕组介质损耗因素测量（tanδ）、绕组对地及绕组间的电容量测量6绕组电阻 >> button")

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
        if t['code'] == -1:
            print('绑定关系已存在')

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span")

    # Click text=工位2工位3工位4工位5工位6工位7工位8工位9工位10工位11工位12工位13工位14工位15工位16工位17工位18工位19工位20工位21工位22
    page.click("text=工位2工位3工位4工位5工位6工位7工位8工位9工位10工位11工位12工位13工位14工位15工位16工位17工位18工位19工位20工位21工位22")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings"):
    with page.expect_response("**/api/v1/test_station_bindings?test_item_id=39") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        print(t['data']['list'][1]['test_area'])
        if t['data']['list'][1]['test_area'] == "收发室":
            print("新增试验项目成功")

    print("试验项目编辑：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")

    # Click text=编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除 >> button")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click li:nth-child(6) .ant-select-tree-switcher
    page.click("li:nth-child(6) .ant-select-tree-switcher")

    # Click span:has-text("油化工位")
    page.click("span:has-text(\"油化工位\")")

    with page.expect_response("**/api/v1/test_station_bindings/22") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('修改后的绑定关系已存在')

    # Click text=编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除 >> button")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span")

    # Click text=工位2
    page.click("text=工位2")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings"):
    with page.expect_response("**/api/v1/test_station_bindings/22") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['test_area'] == "收发室"):
            print('编辑试验项目成功！')
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")

    print("工位绑定删除：")
    # Click :nth-match(:text("删除"), 5)
    page.click(":nth-match(:text(\"删除\"), 5)")

    page.click("button:has-text(\"确定\")")

    print("删除成功")
    # with page.expect_response("**/api/v1/test_station_bindings/40") as response_info:
    #     t = response_info.value.json()
    #     print(t)
    #     if (t['code'] == 0):
    #         print('删除绑定关系成功')

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
    # -----------------------------------------------------------------------------------------------------------------------------------------




    print("判断标准新增:")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings")

    # Click text=判断标准

    with page.expect_navigation():
        page.click("text=判断标准")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")
    # Click button:has-text("新增")

    page.click("button:has-text(\"新增\")")

    # Click form div div div >> :nth-match(div:has-text("请选择"), 5)
    page.click("form div div div >> :nth-match(div:has-text(\"请选择\"), 5)")

    # Click text=油浸式变压器
    page.click("text=油浸式变压器")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "111")

    # Click button:has-text("新增")
    with page.expect_response("**/api/v1/criteria_bindings") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()

        if (t['data']['device_category'] == '油浸式变压器' and t['data']['device_category_id'] == 5):
            print("新增判断标准成功")

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
        if (t['code'] == -1):
            print('绑定关系已存在')

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings

    print("判断标准编辑：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button
    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click span:has-text("油浸式变压器")
    page.click("span:has-text(\"油浸式变压器\")")

    # Click :nth-match(:text("非晶合金油浸式变压器"), 2)
    page.click(":nth-match(:text(\"非晶合金油浸式变压器\"), 2)")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/criteria_bindings/24") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1) and t['message'] == '修改后的绑定关系已存在':
            print('已存在相同名称的企业')

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button
    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click span:has-text("油浸式变压器")
    page.click("span:has-text(\"油浸式变压器\")")

    # Click text=箱变（干式）
    page.click("text=箱变（干式）")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings"):
    with page.expect_response("**/api/v1/criteria_bindings/24") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['device_category'] == '箱变（干式）' and t['data']['device_category_id'] == 116):
            print('编辑成功！')

    print("判断标准删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(2) .text-button")

    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/criteria_bindings/28") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除企业成功')





    print("判断标准新增:")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/standard-bindings")

    # Click text=判断标准
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings"):
    with page.expect_navigation():
        page.click("text=判断标准")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")
    # Click button:has-text("新增")

    page.click("button:has-text(\"新增\")")

    # Click form div div div >> :nth-match(div:has-text("请选择"), 5)
    page.click("form div div div >> :nth-match(div:has-text(\"请选择\"), 5)")

    # Click text=油浸式变压器
    page.click("text=油浸式变压器")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "111")

    # Click button:has-text("新增")
    with page.expect_response("**/api/v1/criteria_bindings") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['device_category'])
        # print(t['data']['device_category_id'])
        if (t['data']['device_category'] == '油浸式变压器' and t['data']['device_category_id'] == 5):
            print("新增判断标准成功")

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
        if (t['code'] == -1):
            print('绑定关系已存在')

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings


    print("判断标准编辑：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button
    page.click( ".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click span:has-text("油浸式变压器")
    page.click("span:has-text(\"油浸式变压器\")")

    # Click :nth-match(:text("非晶合金油浸式变压器"), 2)
    page.click(":nth-match(:text(\"非晶合金油浸式变压器\"), 2)")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/criteria_bindings/24") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1) and t['message'] == '修改后的绑定关系已存在':
            print('已存在相同名称的企业')

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button
    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click span:has-text("油浸式变压器")
    page.click("span:has-text(\"油浸式变压器\")")

    # Click text=箱变（干式）
    page.click("text=箱变（干式）")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings"):
    with page.expect_response("**/api/v1/criteria_bindings/24") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['device_category'] == '箱变（干式）' and t['data']['device_category_id'] == 116):
            print('编辑成功！')

    print("判断标准删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(2) .text-button")
    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/criteria-bindings"):

    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/criteria_bindings/28") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除企业成功')








    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
