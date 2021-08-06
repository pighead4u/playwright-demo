# 试验方案设置
# 测试试验方案设置的增删改查
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    print("test_scheme_test_search start")
    page = context.new_page()
    _test_search(page)
    page.close()
    print("test_scheme_test_search end")

    print("test_scheme_test_create start")
    page = context.new_page()
    _test_create(page)
    page.close()
    print("test_scheme_test_create end")

    print("test_scheme_test_update start")
    page = context.new_page()
    _test_update(page)
    page.close()
    print("test_scheme_test_update end")

    print("test_scheme_test_delete start")
    page = context.new_page()
    _test_delete(page)
    page.close()
    print("test_scheme_test_delete end")

    print("test_scheme_test_inclusion_priority start")
    page = context.new_page()
    _test_inclusion_priority(page)
    page.close()
    print("test_scheme_test_inclusion_priority end")

    page.close()
    context.close()
    browser.close()


# 测试两种情况：
# 1、查询已经存在的国家标准设置
# 2、查询未存在的国家标准设置
def _test_search(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "试验方案8")
    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/test_plans?name=%E8%AF%95%E9%AA%8C%E6%96%B9%E6%A1%888") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data']['list'][0]['name'] == '试验方案8', Exception("查询已存在的试验方案设置失败！！！")
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
        assert t['code'] == 0, Exception("查询未存在的试验方案设置失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans


# 测试两种情况：
# 1、创建已经存在的试验方案，创建失败
# 2、创建未存在的试验方案，创建成功
def _test_create(page):
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
        assert t['data']['name'] == "试验方案11", Exception("创建新的试验方案设置失败!!!")
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
        assert t['code'] == -1, Exception("不存在相同名称的试验方案设置！！！")

# 测试两种情况：
# 1、修改为已经存在的试验方案
# 2、修改为未存在的试验方案
def _test_update(page):
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
        assert t['code'] == -1, Exception("修改后的试验方案设置已存在，测试用例失败！！！")
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")
    # Click text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.click("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]")
    # Fill text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.fill("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]", "试验方案40")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans"):
    with page.expect_response("**/api/v1/test_plans/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "试验方案40", Exception("修改后的国家标准设置已存在，测试用例失败！！！")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(3) .ant-space div:nth-child(1) .text-button")
    # Click text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.click("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]")
    # Fill text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder="请输入"]
    page.fill("text=试验方案名称试验方案编码设备种类(单选)低压电缆分支箱请选择描述 >> [placeholder=\"请输入\"]", "试验方案4")
    page.click("button:has-text(\"确定\")")


# 测试删除功能是否成功
def _test_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "试验方案11")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans"):
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/test_plans/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0, Exception("删除试验方案失败！！！")


# 测试入选优先级功能
def _test_inclusion_priority(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans/49/test-item-bindings")
    # Click button:has-text("新增入选项目优先级")
    page.click("button:has-text(\"新增入选项目优先级\")")
    # Click button:has-text("新增入选项目优先级")
    page.click("button:has-text(\"新增入选项目优先级\")")
    # Click text=温升试验
    page.click("text=温升试验")
    # Click text=入选项目 - 优先级1暂无数据入选项目 - 优先级2暂无数据新增入选项目优先级 >> button
    page.click("text=入选项目 - 优先级1暂无数据入选项目 - 优先级2暂无数据新增入选项目优先级 >> button")
    # Click text=温升试验（干变）
    page.click("text=温升试验（干变）")
    # Click text=入选项目 - 优先级1温升试验入选项目 - 优先级2暂无数据新增入选项目优先级 >> :nth-match(button, 3)
    page.click("text=入选项目 - 优先级1温升试验入选项目 - 优先级2暂无数据新增入选项目优先级 >> :nth-match(button, 3)")
    page.click("button:has-text(\"保存\")")
    with page.expect_response("**/api/v1/test_item_bindings/batch") as response_info:
        t = response_info.value.json()
        assert t['data'][0]['test_item'] == '温升试验', \
            Exception("入选项目失败！！！")
        assert t['data'][1]['test_item'] == "温升试验（干变）", \
            Exception("入选项目失败！！！")
    page.check("text=入选项目 - 优先级1温升试验 >> input[type=\"checkbox\"]")
    # Click text=入选项目 - 优先级1温升试验入选项目 - 优先级2温升试验（干变）新增入选项目优先级 >> :nth-match(button, 2)
    page.click("text=入选项目 - 优先级1温升试验入选项目 - 优先级2温升试验（干变）新增入选项目优先级 >> :nth-match(button, 2)")
    page.click("button:has-text(\"保存\")")
    with page.expect_response("**/api/v1/test_item_bindings/batch") as response_info:
        t = response_info.value.json()
        assert t['data'][0]['priority'] == 2, \
            Exception("入选项目失败！！！")
        assert t['data'][0]['test_item'] == "温升试验（干变）", \
            Exception("入选项目失败！！！")
    page.check("text=入选项目 - 优先级2温升试验（干变） >> input[type=\"checkbox\"]")
    # Click text=入选项目 - 优先级1暂无数据入选项目 - 优先级2温升试验（干变）新增入选项目优先级 >> :nth-match(button, 4)
    page.click("text=入选项目 - 优先级1暂无数据入选项目 - 优先级2温升试验（干变）新增入选项目优先级 >> :nth-match(button, 4)")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans/49/test-item-bindings"):

    page.click("button:has-text(\"保存\")")

