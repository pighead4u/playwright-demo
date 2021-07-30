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
#----------------------------------------------------------------------------------------------------------------------








    print("编辑：")
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
            print('编辑成功！')

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
