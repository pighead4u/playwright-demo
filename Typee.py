import time

from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    print("查询：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "变压器")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click text=序号设备种类名称1变压器 >> [aria-label="展开行"]
    with page.expect_response("**/api/v1/device_categories/tree?name=%E5%8F%98%E5%8E%8B%E5%99%A8&code=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if((t['data'][0]['name']) == '变压器' and t['data'][0]['children'][1]['name'] == '非晶合金油浸式变压器'):
             print('查询成功')

        # print(t['data'][0]['children'][1]['name'])
        # if (t['data']['list'][0]['name'] == '变压器'):
        #     print('查询成功')
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "变压器1")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/device_categories/tree?name=%E5%8F%98%E5%8E%8B%E5%99%A81&code=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if (t['data'] == []):
            print("暂无数据")

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click input[role="combobox"]
    page.click("input[role=\"combobox\"]")

    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/device_categories/tree?name=&code=&device_category_type_id=7") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if ((t['data'][0]['name']) == '变压器' and t['data'][-1]['name'] == '一二次融合断路器'):
            print('查询成功')

    # Click button:has-text("重置")
    # page.click("button:has-text(\"重置\")")
    #
    # Click button:has-text("查询")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories"):
    # with page.expect_navigation():
    #     page.click("button:has-text(\"查询\")")

    print("新增：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.click("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]")

    # Fill text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "变压器")

    # Click text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> input[role="combobox"]
    page.click("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> input[role=\"combobox\"]")

    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")

    # Click text=额外参数请选择 >> input[role="combobox"]
    page.click("text=额外参数请选择 >> input[role=\"combobox\"]")

    # Click :nth-match(:text("( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器"), 2)
    page.click(":nth-match(:text(\"( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器\"), 2)")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/device_categories") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称设备种类')

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.click("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]")

    # Fill text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "变压器2")

    # Click text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> input[role="combobox"]
    page.click("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> input[role=\"combobox\"]")

    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")

    # Click text=额外参数请选择 >> input[role="combobox"]
    page.click("text=额外参数请选择 >> input[role=\"combobox\"]")

    # Click :nth-match(:text("( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器"), 2)
    page.click(":nth-match(:text(\"( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器\"), 2)")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories"):
    with page.expect_response("**/api/v1/device_categories") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['data']['name'] == "变压器2"):
            print("新增成功")

    print("新增子类：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")
    # page.wait_for_selector('.ant-table-body')
    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.click("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]")

    # Press CapsLock
    page.press("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "CapsLock")

    # Fill text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "JP")

    # Press CapsLock
    page.press("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "CapsLock")

    # Fill text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "JP柜")

    # Click text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> input[role="combobox"]
    page.click("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> input[role=\"combobox\"]")

    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")

    # Click text=额外参数请选择 >> input[role="combobox"]
    page.click("text=额外参数请选择 >> input[role=\"combobox\"]")

    # Click text=( blq ) 无间隙避雷器、有间隙避雷器
    page.click("text=( blq ) 无间隙避雷器、有间隙避雷器")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/device_categories") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的设备种类')

    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.click("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]")

    # Press CapsLock
    page.press("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "CapsLock")

    # Fill text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "JP")

    # Press CapsLock
    page.press("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "CapsLock")

    # Fill text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "JP柜1")

    # Click text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> input[role="combobox"]
    page.click("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> input[role=\"combobox\"]")

    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")

    # Click text=额外参数请选择 >> input[role="combobox"]
    page.click("text=额外参数请选择 >> input[role=\"combobox\"]")

    # Click text=( blq ) 无间隙避雷器、有间隙避雷器
    page.click("text=( blq ) 无间隙避雷器、有间隙避雷器")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories"):
    with page.expect_response("**/api/v1/device_categories") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['data']['name'] == "JP柜1"):
            print("新增子类成功")

    print("编辑：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button
    #page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button")
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(1) .ant-space div:nth-child(2) .text-button")
    # Click text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.click("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]")

    # Fill text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]", "J")

    # Press CapsLock
    page.press("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]", "CapsLock")

    # Fill text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]", "JP")

    # Press CapsLock
    page.press("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]", "CapsLock")

    # Fill text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]", "JP柜")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/device_categories/1") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的设备种类')

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button
    #page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button")
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(1) .ant-space div:nth-child(2) .text-button")
    # Click text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.click("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]")

    # Fill text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]", "变压器1")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories"):
    with page.expect_response("**/api/v1/device_categories/1") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['data']['name'] == "变压器1"):
            print("编辑成功")
    print("删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(14) .ant-space div:nth-child(3) .text-button")
    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories"):

    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/device_categories/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除设备种类成功')

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)