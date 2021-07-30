from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    print("国标查询：")
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
        # print(t['data']['list'][0]['name'])
        if (t['data']['list'][0]['name'] == '国标1'):
            print('查询成功')

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
        # print(t['data']['list'][0]['name'])
        # print(t)
        # print(t['data']['total'])
        if (t['data']['total'] == 0):
            print('暂无数据')

    # Click button:has-text("重置")
    page.click("button:has-text(\"重置\")")

    # Click button:has-text("查询")
    page.click("button:has-text(\"查询\")")


    print("国际标准新增：")

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

    # Click .ant-calendar-cell.ant-calendar-selected-end-date .ant-calendar-date
    page.click(".ant-calendar-cell.ant-calendar-selected-end-date .ant-calendar-date")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/standards") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的国标')

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

    # Click .ant-calendar-cell.ant-calendar-selected-end-date .ant-calendar-date
    page.click(".ant-calendar-cell.ant-calendar-selected-end-date .ant-calendar-date")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards"):
    with page.expect_response("**/api/v1/standards") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['data']['name']=="国标10"):
            print('新增国家标准设置成功')


    print("国标编辑：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards")

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(6) .ant-space div:nth-child(1) .text-button")
    # Click text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.click("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]")

    # Fill text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.fill("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]", "国标2")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/standards/67") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('已存在相同名称的国标')

    # Click .ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(6) .ant-space div:nth-child(1) .text-button")
    # Click text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.click("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]")

    # Fill text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.fill("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]", "国标11")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards"):
    with page.expect_response("**/api/v1/standards/67") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['data']['name'] == "国标11" and t['data']['code'] == "1"):
            print('修改国家标准设置成功')
    # page.click(".ant-table-body-inner .ant-table-fixed .ant-table-tbody .ant-table-row.table-striped.ant-table-row-hover .ant-table-row-cell-break-word .ant-space div .text-button")
    page.click(".ant-table-fixed-right .ant-table-tbody tr:nth-child(6) .ant-space div:nth-child(1) .text-button")
    # Click text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]

    page.click("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]")

    # Fill text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder="请输入"]
    page.fill("text=国标名称编码简称描述有效期 ~ 国标上传上传文件 >> [placeholder=\"请输入\"]", "国标1")

    page.click("button:has-text(\"确定\")")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards"):
    # with page.expect_response("**/api/v1/standards/67") as response_info:
    #     page.click("button:has-text(\"确定\")")
    #     t = response_info.value.json()
    #     if (t['data']['name'] == "国标11" and t['data']['code'] == "1"):
    #         print('修改国家标准设置成功')

    print("国家标准删除：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards")

    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")

    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "国标10")

    page.click("button:has-text(\"查询\")")

    # Click :nth-match(:text("删除"), 3)
    page.click(":nth-match(:text(\"删除\"), 3)")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/standards"):
    page.click("button:has-text(\"确定\")")

    with page.expect_response("**/api/v1/standards/*") as response_info:
        t = response_info.value.json()
        if (t['code'] == 0):
            print('删除国标设置成功')
    page.close()

    # ---------------------
    context.close()
    browser.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)