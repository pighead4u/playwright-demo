import datetime

_company = f"单位{datetime.datetime.now()}"


# 委托单位管理
# 测试委托单位的增删改查
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()

    print("_test_search start")
    _test_search(page)
    print("_test_search end")

    print("_test_create start")
    _test_create(page)
    print("_test_create end")

    print("_test_update start")
    _test_update(page)
    print("_test_update end")

    print("_test_delete start")
    _test_delete(page)
    print("_test_delete end")

    page.close()
    context.close()
    browser.close()


def _test_delete(page):
    pass


# 测试两种情况：
# 1、修改为已经存在的单位
# 2、修改为未存在的单位
def _test_update(page):
    # 编辑
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/2")
    # Click text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")
    # Click text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")
    # Fill text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "单位2")
    # Press ArrowLeft
    page.press("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "ArrowLeft")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/companies/27") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("修改后的委托单位已经存在，测试用例失败!!!")

    # Click text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")
    # Fill text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "单位13")
    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/2"):
    # with page.expect_navigation():
    with page.expect_response("**/api/v1/companies/27") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "单位13", Exception("修改后的委托单位已经存在，测试用例失败!!!")

    # 复原修改后的数据
    page.click("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")
    # Fill text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "单位1")
    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/2"):
    # with page.expect_navigation():
    with page.expect_response("**/api/v1/companies/27") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == "单位1", Exception("修改后的委托单位已经存在，测试用例失败!!!")


# 测试两种情况：
# 1、查询已经存在的单位
# 2、查询未存在的单位
def _test_search(page):
    # 查询
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/2")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    company = "单位1"
    page.fill("[placeholder=\"请输入\"]", company)
    with page.expect_response("**/api/v1/companies?type=2&name=%E5%8D%95%E4%BD%8D1") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        # print(t['data']['list'][0]['name'])
        assert t['data']['list'][0]['name'] == company, Exception("查询已存在的委托单位失败！！！")

    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Press ArrowRight
    page.press("button:has-text(\"查询\")", "ArrowRight")
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "单位100")
    with page.expect_response("**/api/v1/companies?type=2&name=%E5%8D%95%E4%BD%8D100") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data']['total'] == 0, Exception("查询不存在的委托单位失败！！！")


# 测试两种情况：
# 1、创建已经存在的单位，创建失败
# 2、创建未存在的单位，创建成功
def _test_create(page):
    # 新增
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "单位1")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 2)")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 2)", "杭州")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 5)")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 5)", "12345677654")
    with page.expect_response("**/api/v1/companies") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("不存在相同名称企业")

    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/2")
    page.click("button:has-text(\"新增\")")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]

    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", _company)
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 2)")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 2)", "杭州")
    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 5)")
    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 5)", "12345677654")
    # print(t)
    with page.expect_response("**/api/v1/companies") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == _company, Exception("创建新的委托单位失败!!!")
