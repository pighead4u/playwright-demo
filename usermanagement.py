from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/system-setting/users
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/system-setting/users")

    print("用户查询：")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "b")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/users?user_name=b") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if (t['data']['list'][0]['user_name'] == 'b'):
            print('查询用户成功')

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
        if (t['code'] == 0):
            print('暂无数据')

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    print("用户新增：")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=头像上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.click("text=头像上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]")

    # Fill text=头像上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.fill("text=头像上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]", "qqq")

    # Click text=头像ccc上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> :nth-match([placeholder="请输入"], 2)
    page.click("text=头像ccc上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> :nth-match([placeholder=\"请输入\"], 2)")

    # Fill text=头像ccc上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> :nth-match([placeholder="请输入"], 2)
    page.fill("text=头像ccc上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> :nth-match([placeholder=\"请输入\"], 2)", "111")

    # Click text=男
    page.click("text=男")

    # Click text=女
    page.click("text=女")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=头像上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.click("text=头像上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]")

    # Fill text=头像上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.fill("text=头像上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]", "c")

    # Click text=头像c上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> :nth-match([placeholder="请输入"], 2)
    page.click("text=头像c上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> :nth-match([placeholder=\"请输入\"], 2)")

    # Fill text=头像c上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> :nth-match([placeholder="请输入"], 2)
    page.fill("text=头像c上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> :nth-match([placeholder=\"请输入\"], 2)", "hhh")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")

    print("用户编辑：")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.click("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]")

    # Fill text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.fill("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]", "c")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.click("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]")

    # Fill text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.fill("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]", "bbb")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")

    # Click text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.click("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]")

    # Fill text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder="请输入"]
    page.fill("text=头像bxxx上传图片头像用户名昵称性别男部门请选择电话号码电子邮件联系地址签名文件上传文件 >> [placeholder=\"请输入\"]", "b")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/system-setting/users"):
    with page.expect_navigation():
        page.click("button:has-text(\"确定\")")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)