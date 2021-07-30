from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    #查询
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "变压器厂")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/companies?type=1&name=%E5%8F%98%E5%8E%8B%E5%99%A8%E5%8E%82") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        # print(t['data']['list'][0]['name'])
        if (t['data']['list'][0]['name'] == '变压器厂'):
            print('查询成功')

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "变压器厂1")

    # Press ArrowRight
    page.press("[placeholder=\"请输入\"]", "ArrowRight")

    # Click button:has-text("查询")
    with page.expect_response("**/api/v1/companies?type=1&name=%E5%8F%98%E5%8E%8B%E5%99%A8%E5%8E%821") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        if (t['data']['total'] == 0):
            print("暂无数据")

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")




    #新增
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")

    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "12312")

    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 2)")

    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 2)", "幅度恭亲王")

    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 5)")

    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 5)", "547558")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/companies") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] != -1):
            print('code 不等于 -1')
        elif (t['message'] != '已存在相同名称的企业'):
            print('message 不等于 已存在相同名称的企业')
        else:
            print('已存在相同名称企业')

    # Click text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")

    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "123845611")

    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 2)")

    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 2)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 2)", "幅度恭亲王")

    # Click text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 5)")

    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder="请输入"], 5)
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> :nth-match([placeholder=\"请输入\"], 5)", "547558")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/companies") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        if (t['data']['name'] == "123845611"):
            print("新增成功")


    #编辑
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1")

    page.click("text=编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除编辑删除 >> button")

    # Click text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")

    # Fill text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "开关公司")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/companies/29") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] != -1):
            print('code 不等于 -1')
        elif (t['message'] != '已存在相同名称的企业'):
            print('message 不等于 已存在相同名称的企业')
        else:
            print('已存在相同名称的企业')

    # Click text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")

    # Fill text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=编辑名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "撒旦撒旦和")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1"):
    with page.expect_response("**/api/v1/companies/29") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['name'] == "撒旦撒旦和"):
            print('编辑成功！')
    #删除
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1")

    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(7) .ant-space div:nth-child(2) .text-button")

    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/companies/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除企业成功')

    print('删除企业成功')
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/1")
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)