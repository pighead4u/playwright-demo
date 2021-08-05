import datetime

_company = f"开关公司{datetime.datetime.now()}"


# 生产单位管理
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    print("manufactory_test_search start")
    page = context.new_page()
    _test_search(page)
    page.close()
    print("manufactory_test_search end")

    print("manufactory_test_create start")
    page = context.new_page()
    _test_create(page)
    page.close()
    print("manufactory_test_create end")

    print("manufactory_test_update start")
    page = context.new_page()
    _test_update(page)
    page.close()
    print("manufactory_test_update end")

    print("manufactory_test_delete start")
    page = context.new_page()
    _test_delete(page)
    page.close()
    print("manufactory_test_delete end")

    page.close()
    context.close()
    browser.close()


# 待后端倒序排列后处理
def _test_delete(page):
    pass


# 测试两种情况：
# 1、修改为已经存在的单位
# 2、修改为未存在的单位
def _test_update(page):
    # 编辑
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1")
    # Click text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(2) .ant-space div:nth-child(1) .text-button")
    # page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")
    # Click text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']")
    # Fill text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']", "开关公司")
    # Press ArrowLeft
    page.press("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']", "ArrowLeft")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/companies/*") as response_info:
        page.click("button:has-text('确定')")
    t = response_info.value.json()
    assert t['code'] == -1, Exception("修改后的生产厂家已经存在，测试用例失败!!!")
    page.click("button:has-text('取消')")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(1) .ant-space div:nth-child(1) .text-button")
    # Click text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']")
    # Fill text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']", "单位13")
    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1"):
    # with page.expect_navigation():
    with page.expect_response("**/api/v1/companies/*") as response_info:
        page.click("button:has-text('确定')")
        t = response_info.value.json()
        assert t['data']['name'] == "单位13", Exception("修改后的生产厂家已经存在，测试用例失败!!!")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(1) .ant-space div:nth-child(1) .text-button")
    # 复原修改后的数据
    page.click("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']")
    # Fill text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']", "开关公司")
    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1"):
    # with page.expect_navigation():
    with page.expect_response("**/api/v1/companies/*") as response_info:
        page.click("button:has-text('确定')")
        t = response_info.value.json()
        assert t['data']['name'] == "开关公司", Exception("修改后的生产厂家已经存在，测试用例失败!!!")


# 测试两种情况：
# 1、查询已经存在的单位
# 2、查询未存在的单位
def _test_search(page):
    # 查询
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1")
    # Click [placeholder="请输入"]
    page.click("[placeholder='请输入']")
    # Fill [placeholder="请输入"]
    company = "开关公司"
    page.fill("[placeholder='请输入']", company)
    with page.expect_response("**/api/v1/companies?type=1&name=%E5%BC%80%E5%85%B3%E5%85%AC%E5%8F%B8") as response_info:
        page.click("button:has-text('查询')")
    t = response_info.value.json()
    assert t['data']['list'][0]['name'] == company, Exception("查询已存在的生产厂家失败！！！")

    page.click("button:has-text('重置')")
    # Click button:has-text("查询")
    page.click("button:has-text('查询')")
    # Press ArrowRight
    page.press("button:has-text('查询')", "ArrowRight")
    page.click("[placeholder='请输入']")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder='请输入']", "单位100")
    with page.expect_response("**/api/v1/companies?type=1&name=%E5%8D%95%E4%BD%8D100") as response_info:
        page.click("button:has-text('查询')")
    t = response_info.value.json()
    assert t['data']['total'] == 0, Exception("查询不存在的生产厂家失败！！！")


# 测试两种情况：
# 1、创建已经存在的单位，创建失败
# 2、创建未存在的单位，创建成功
def _test_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1")

    # 新增
    # Click button:has-text("新增")
    page.click("button:has-text('新增')")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']", "开关公司")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder='请输入'], 2)")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder='请输入'], 2)", "杭州")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder='请输入'], 5)")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder='请输入'], 5)", "12345677654")
    with page.expect_response("**/api/v1/companies") as response_info:
        page.click("button:has-text('确定')")
    t = response_info.value.json()
    assert t['code'] == -1, Exception("不存在相同名称企业")
    page.click("button:has-text('取消')")

    page.click("button:has-text('新增')")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]

    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder='请输入']", _company)
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder='请输入'], 2)")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder='请输入'], 2)", "杭州")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder='请输入'], 5)")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder='请输入'], 5)", "12345677654")
    # print(t)
    with page.expect_response("**/api/v1/companies") as response_info:
        page.click("button:has-text('确定')")
    t = response_info.value.json()
    assert t['data']['name'] == _company, Exception("创建新的生产厂家失败!!!")
