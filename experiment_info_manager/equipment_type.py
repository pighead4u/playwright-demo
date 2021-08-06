# 设备种类设置
# 测试设备种类设置的增删改查
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    print("equipment_type_test_search start")
    page = context.new_page()
    _test_search(page)
    page.close()
    print("equipment_type_test_search end")

    print("equipment_type_test_create start")
    page = context.new_page()
    _test_create(page)
    page.close()
    print("equipment_type_test_create end")

    print("equipment_type_test_children_create start")
    page = context.new_page()
    _test_children_create(page)
    page.close()
    print("equipment_type_test_children_create end")

    print("equipment_type_test_children_delete start")
    page = context.new_page()
    _test_children_delete(page)
    page.close()
    print("equipment_type_test_children_delete end")

    print("equipment_type_test_update start")
    page = context.new_page()
    _test_update(page)
    page.close()
    print("equipment_type_test_update end")

    print("equipment_type_test_delete start")
    page = context.new_page()
    _test_delete(page)
    page.close()
    print("equipment_type_test_delete end")

    page.close()
    context.close()
    browser.close()


# 测试两种情况：
# 1、查询已经存在的设备种类设置
# 2、查询未存在的设备种类设置
def _test_search(page):
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "变压器")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click text=序号设备种类名称1变压器 >> [aria-label="展开行"]
    with page.expect_response(
            "**/api/v1/device_categories/tree?name=%E5%8F%98%E5%8E%8B%E5%99%A8&code=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data'][0]['name'] == '变压器', Exception("查询已存在的设备种类失败！！！")
        assert t['data'][0]['children'][1]['name'] == '非晶合金油浸式变压器', Exception("查询已存在的设备种类失败！！！")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "变压器1")
    # Click button:has-text("查询")
    with page.expect_response(
            "**/api/v1/device_categories/tree?name=%E5%8F%98%E5%8E%8B%E5%99%A81&code=") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data'] == [], Exception("查询未存在的设备种类设置失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click input[role="combobox"]
    page.click("input[role=\"combobox\"]")
    # Click .ant-select-item-option-content
    page.click(".ant-select-item-option-content")
    # Click button:has-text("查询")
    with page.expect_response(
            "**/api/v1/device_categories/tree?name=&code=&device_category_type_id=7") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data'][0]['name'] == '变压器' and t['data'][-1]['name'] == '一二次融合断路器', Exception("查询已存在的设备种类失败！！！")


# 测试两种情况：
# 1、创建已经存在的设备种类，创建失败
# 2、创建未存在的设备种类，创建成功
def _test_create(page):
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
        assert t['code'] == -1, Exception("不存在相同名称的设备种类！！！")
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
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories"):
    with page.expect_response("**/api/v1/device_categories") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "变压器2", Exception("创建新的设备种类失败！！！")


# 测试两种情况：
# 1、创建已经存在的设备种类，创建失败
# 2、创建未存在的设备种类，创建成功
def _test_children_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")

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
        assert t['code'] == -1, Exception("不存在相同名称的设备种类！！")

    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # Click text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.click("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]")
    # Press CapsLock
    page.press("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "CapsLock")
    # Fill text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型请选择额外参数请选择描述图片 上传 >> [placeholder=\"请输入\"]", "JP")
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
    with page.expect_response("**/api/v1/device_categories") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "JP柜1", Exception("创建新的设备种类失败！！！")


# 测试设备种类子类删除功能是否成功
def _test_children_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "JP")
    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "JP柜1")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click text=序号设备种类名称1JP柜 >> [aria-label="展开行"]
    page.click("text=序号设备种类名称1JP柜 >> [aria-label=\"展开行\"]")
    # Click :nth-match(:text("删除"), 5)
    page.click(":nth-match(:text(\"删除\"), 5)")
    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/device_categories/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0, Exception("删除设备种类失败！！！")


# 测试两种情况：
# 1、修改已经存在的设备种类，创建失败
# 2、修改未存在的设备种类，创建成功
def _test_update(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div:nth-child(2) .text-button")
    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(1) .ant-space div:nth-child(2) .text-button")
    # Click text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.click(
        "text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]")
    # Fill text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]",
              "J")
    # Press CapsLock
    page.press(
        "text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]",
        "CapsLock")
    # Fill text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]",
              "JP")
    # Press CapsLock
    page.press(
        "text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]",
        "CapsLock")
    # Fill text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]",
              "JP柜")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/device_categories/1") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("修改后的设备种类已存在，测试用例失败！！！")

    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(1) .ant-space div:nth-child(2) .text-button")
    # Click text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.click(
        "text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]")
    # Fill text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]",
              "变压器1")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories"):
    with page.expect_response("**/api/v1/device_categories/1") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "变压器1", Exception("修改后的设备种类已存在，测试用例失败！！！")

    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(1) .ant-space div:nth-child(2) .text-button")
    # Click text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.click(
        "text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]")
    # Fill text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder="请输入"]
    page.fill("text=设备种类名称设备种类编码设备种类类型一次设备额外参数( byq1 ) 干式变压器、油浸式变压器、非晶合金油浸式变压器、有载调压变压器描述图片 上传 >> [placeholder=\"请输入\"]",
              "变压器")
    page.click("button:has-text(\"确定\")")


# 测试删除功能是否成功
def _test_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/device-categories")
    page.click(
        ".ant-table-body-inner .ant-table-fixed .ant-table-tbody tr:nth-child(14) .ant-space div:nth-child(3) .text-button")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/device_categories/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0, Exception("删除设备种类失败！！！")
