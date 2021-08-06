# 用户管理设置
# 测试用户管理设置的增删改查
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    print("user_management_test_search start")
    page = context.new_page()
    _test_search(page)
    page.close()
    print("user_management_test_search end")

    print("user_management_test_create start")
    page = context.new_page()
    _test_create(page)
    page.close()
    print("user_management_test_create end")

    print("user_management_test_update start")
    page = context.new_page()
    _test_update(page)
    page.close()
    print("user_management_test_update end")

    print("user_management_test_delete start")
    page = context.new_page()
    _test_delete(page)
    page.close()
    print("user_management_test_delete end")

    page.close()
    context.close()
    browser.close()


# 测试两种情况：
# 1、查询已经存在的用户管理
# 2、查询未存在的用户管理
def _test_search(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/system-setting/users")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "b")
    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/users?user_name=b") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['data']['list'][0]['user_name'] == 'b', Exception("查询已存在的用户失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "b1")
    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/users?user_name=b1") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        assert t['code'] == 0, Exception("查询未存在的国家标准设置失败！！！")
    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")
    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")


# 测试两种情况：
# 1、创建已经存在的用户，创建失败
# 2、创建未存在的用户，创建成功
def _test_create(page):
    pass


# 测试两种情况：
# 1、修改为已经存在的用户管理
# 2、修改为未存在的用户管理
def _test_update(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/system-setting/users")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(1) .text-button")
    # Click text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.click("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]")

    page.fill("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]", "c")

    with page.expect_response("**/api/v1/users/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("修改后的用户已存在，测试用例失败！！！")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(1) .text-button")

    page.click("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]")

    page.fill("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]", "bbb")

    with page.expect_response("**/api/v1/users/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['user_name'] == 'bbb', Exception("修改后的用户已存在，测试用例失败！！！")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(4) .ant-space div:nth-child(1) .text-button")

    page.click("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]")

    page.fill("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]", "b")

    page.click("button:has-text(\"确定\")")


# 测试用户管理删除是否成功：
def _test_delete(page):
    pass
