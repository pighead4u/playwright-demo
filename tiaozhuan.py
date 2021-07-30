from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    print("工位绑定新增：")
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items")

    # Click text=1温升试验2温升试验（干变）3温升试验（一二次融合）4绕组对地及绕组间直流绝缘电阻测量5绕组介质损耗因素测量（tanδ）、绕组对地及绕组间的电容量测量6绕组电阻 >> button
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings"):
    with page.expect_navigation():
        page.click("text=1温升试验2温升试验（干变）3温升试验（一二次融合）4绕组对地及绕组间直流绝缘电阻测量5绕组介质损耗因素测量（tanδ）、绕组对地及绕组间的电容量测量6绕组电阻 >> button")

    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click li:nth-child(5) .ant-select-tree-switcher
    page.click("li:nth-child(5) .ant-select-tree-switcher")

    # Click ul[role="group"] >> text=b3
    page.click("ul[role=\"group\"] >> text=b3")

    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/test_station_bindings") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if t['code'] == -1:
            print('绑定关系已存在')

    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span")

    # Click text=工位2工位3工位4工位5工位6工位7工位8工位9工位10工位11工位12工位13工位14工位15工位16工位17工位18工位19工位20工位21工位22
    page.click("text=工位2工位3工位4工位5工位6工位7工位8工位9工位10工位11工位12工位13工位14工位15工位16工位17工位18工位19工位20工位21工位22")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings"):
    with page.expect_response("**/api/v1/test_station_bindings?test_item_id=39") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t['data']['name'])
        print(t['data']['list'][1]['test_area'])
        if t['data']['list'][1]['test_area'] == "收发室":
            print("新增成功")

    print("工位绑定删除：")
    # Click :nth-match(:text("删除"), 5)
    page.click(":nth-match(:text(\"删除\"), 5)")

    page.click("button:has-text(\"确定\")")

    print("删除成功")
    # with page.expect_response("**/api/v1/test_station_bindings/40") as response_info:
    #     t = response_info.value.json()
    #     print(t)
    #     if (t['code'] == 0):
    #         print('删除绑定关系成功')


    print("编辑：")
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")

    # Click text=编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除 >> button")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click li:nth-child(6) .ant-select-tree-switcher
    page.click("li:nth-child(6) .ant-select-tree-switcher")

    # Click span:has-text("油化工位")
    page.click("span:has-text(\"油化工位\")")

    with page.expect_response("**/api/v1/test_station_bindings/22") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        if (t['code'] == -1):
            print('修改后的绑定关系已存在')

    # Click text=编辑删除编辑删除 >> button
    page.click("text=编辑删除编辑删除 >> button")

    # Click [aria-label="filter select"]
    page.click("[aria-label=\"filter select\"]")

    # Click text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span
    page.click("text=收发室配电房高压试验区综合试验区温升试验区油化室仓库临时试验区 >> span")

    # Click text=工位2
    page.click("text=工位2")

    # Click button:has-text("确定")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings"):
    with page.expect_response("**/api/v1/test_station_bindings/22") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        # print(t)
        if (t['data']['test_area'] == "收发室"):
            print('编辑成功！')
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")

    print("编辑：")


    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
