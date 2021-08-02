from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    print("试验区域查询：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "收发室")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/test_areas?name=%E6%94%B6%E5%8F%91%E5%AE%A4&code=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if (t['data']['list'][0]['name'] == '收发室'):
            print('查询试验区域成功')

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
        if (t['code'] == 0):
            print('暂无数据')

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    print("实验区域新增：")
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
        # print(t['data']['name'])
        if (t['code'] == -1):
            print('已存在相同名称的试验区域')

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

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas"):
    with page.expect_response("**/api/v1/test_areas") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['data']['name'] == "收发室1"):
            print("新增试验区域成功")

    print("实验区域编辑：")
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
        if (t['code'] == -1):
            print('已存在相同名称的试验区域')

    # Click text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")

    # Click text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.click("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]")

    # Fill text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.fill("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]", "仓库1")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas"):
    with page.expect_response("**/api/v1/test_areas/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['name'] == "仓库1"):
            print('编辑试验区域成功！')

    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")

    # Click text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.click("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]")

    # Fill text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder="请输入"]
    page.fill("text=试验区名称试验区编码试验区类型试验区描述 >> [placeholder=\"请输入\"]", "收发室")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas"):

    page.click("button:has-text(\"确定\")")

    print("实验区域删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "收发室1")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas"):
    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/test_areas/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除试验区域成功')

    print("试验区工位新增：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas")

    # Click text=1收发室2配电房3高压试验区4综合试验区5温升试验区6油化室7仓库8临时试验区 >> button
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations"):
    with page.expect_navigation():
        page.click("text=1收发室2配电房3高压试验区4综合试验区5温升试验区6油化室7仓库8临时试验区 >> button")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "工位50")

    # Click :nth-match([placeholder="请输入"], 3)
    page.click(":nth-match([placeholder=\"请输入\"], 3)")

    # Fill :nth-match([placeholder="请输入"], 3)
    page.fill(":nth-match([placeholder=\"请输入\"], 3)", "无")

    # Click .ant-select-selection-overflow
    page.click(".ant-select-selection-overflow")

    # Click :nth-match(:text("test"), 5)
    page.click(":nth-match(:text(\"test\"), 5)")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_stations") as response_info:
       page.click("button:has-text(\"确定\")")
       t = response_info.value.json()
       # print(t['data']['name'])
       if(t['data']['name'] == "工位50"):
            print("新增试验区工位成功")

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
        if (t['code'] == -1):
            print('已存在相同名称的试验工位')

    print("试验区工位编辑：")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "工位5")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_stations/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的试验工位')

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "工位40")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "工位6")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations")

    print("试验区工位删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations")

    # Click a:has-text("3")
    page.click("a:has-text(\"3\")")

    # Click :nth-match(:text("删除"), 5)
    page.click(":nth-match(:text(\"删除\"), 5)")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/test_stations/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除试验工位成功')

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/test-areas/9/test-stations")


    # Close page

    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)