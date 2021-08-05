# 国家标准设置
# 测试国家标准设置的增删改查
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    print("national_standard_test_search start")
    page = context.new_page()
    _test_search(page)
    page.close()
    print("national_standard_test_search end")

    print("national_standard_test_create start")
    page = context.new_page()
    _test_create(page)
    page.close()
    print("national_standard_test_create end")

    print("national_standard_test_update start")
    page = context.new_page()
    _test_update(page)
    page.close()
    print("national_standard_test_update end")

    print("national_standard_test_delete start")
    page = context.new_page()
    _test_delete(page)
    page.close()
    print("national_standard_test_delete end")

    page.close()
    context.close()
    browser.close()

# 测试两种情况：
# 1、查询已经存在的国家标准设置
# 2、查询未存在的国家标准设置
def _test_search(page):
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "国标1")
    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/standards?name=%E5%9B%BD%E6%A0%871") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data']['list'][0]['name'] == '国标1',Exception("查询已存在的国家标准设置失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "国标12")
    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/standards?name=%E5%9B%BD%E6%A0%8712") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data']['total'] == 0,Exception("查询未存在的国家标准设置失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")


# 测试两种情况：
# 1、创建已经存在的单位，创建失败
# 2、创建未存在的单位，创建成功
def _test_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.click("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]")
    # Fill text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.fill("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]", "国标1")
    # Click [placeholder="请选择生效时间"]
    page.click("[placeholder=\"请选择生效时间\"]")
    # Click table[role="grid"] >> text=1
    page.click("table[role=\"grid\"] >> text=1")
    # page.click(".ant-calendar-cell.ant-calendar-selected-end-date .ant-calendar-date")
    page.click(":nth-match(td[role=\"gridcell\"]:has-text(\"16\"), 2)")
    with page.expect_response("**/api/v1/standards") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1,Exception("不存在相同名称的国家标准设置！！！")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.click("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]")
    # Fill text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.fill("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]", "国标10")
    # Click [placeholder="请选择生效时间"]
    page.click("[placeholder=\"请选择生效时间\"]")
    # Click table[role="grid"] >> :nth-match(:text("9"), 2)
    page.click("table[role=\"grid\"] >> :nth-match(:text(\"9\"), 2)")
    # page.click(".ant-calendar-cell.ant-calendar-selected-end-date .ant-calendar-date")
    page.click(":nth-match(td[role=\"gridcell\"]:has-text(\"16\"), 2)")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards"):
    with page.expect_response("**/api/v1/standards") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name']=="国标10",Exception("创建新的国家标准设置失败!!!")


#测试两种情况：
# 1、修改为已经存在的国家标准
# 2、修改为未存在的国家标准
def _test_update(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(6) .ant-space div:nth-child(1) .text-button")
    # Click text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.click("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]")
    page.fill("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]", "国标2")
    with page.expect_response("**/api/v1/standards/67") as response_info:
         page.click("button:has-text(\"确定\")")
         t = response_info.value.json()
         assert t['code'] == -1,Exception("修改后的国家标准设置已存在，测试用例失败！！！")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(6) .ant-space div:nth-child(1) .text-button")
         # Click text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.click("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]")
         # Fill text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.fill("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]", "国标11")

    with page.expect_response("**/api/v1/standards/67") as response_info:
         page.click("button:has-text(\"确定\")")
         t = response_info.value.json()
         assert t['data']['name'] == "国标11" and t['data']['code'] == "1",Exception("修改后的国家标准设置已存在，测试用例失败！！！")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(6) .ant-space div:nth-child(1) .text-button")

    page.click("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]")

    page.fill("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]", "国标1")

    page.click("button:has-text(\"确定\")")

#测试删除功能是否成功
def _test_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "国标10")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/standards/*") as response_info:
         t = response_info.value.json()
         assert t['code'] == 0,Exception("删除国家标准设置失败！！！")

