from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    # 查询
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/2")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "单位1")

    with page.expect_response("**/api/v1/companies?type=2&name=%E5%8D%95%E4%BD%8D1") as response_info:
        page.click("button:has-text(\"查询\")")
        t = response_info.value.json()
        # print(t['data']['list'][0]['name'])
        if(t['data']['list'][0]['name'] =='单位1'):

            print('查询成功')


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
        if(t['data']['total'] == 0):
           print("暂无数据")


    #新增
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
       if (t['code'] == -1):
            print('已存在相同名称企业')
       # print(t)

    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/2")



    page.click("button:has-text(\"新增\")")

    # Click text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.click("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]")

    # Fill text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder="请输入"]
    page.fill("text=新增名称地址邮编联系人联系电话取消确定 >> [placeholder=\"请输入\"]", "单位11")

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
       # print(t['data']['name'])
       if(t['data']['name'] == "单位11"):
            print("新增成功")


     #编辑
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
        if (t['code'] == -1):
            print('已存在相同名称的企业')

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
        # print(t)
        if (t['data']['name'] == "单位13"):
            print('编辑成功！')

    #删除
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/2")


    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(7) .ant-space div:nth-child(2) .text-button")


    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/companies/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除企业成功')


    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/companies/2")

    # time.sleep(1000)
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
