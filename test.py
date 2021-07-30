from playwright.sync_api import sync_playwright
import time


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # 截取API的信息
    def res(response):
        if "http://mes-dev.tunnel.shunjiantech.cn/api/v1/test_items" in response.url:
               arr = response.json()['data']
               print(arr)

    page.on("response", res)

    # Go to http://mes-dev.tunnel.shunjiantech.cn/
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/")

    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/")

    # Click span:has-text("试验信息管理")
    page.click("span:has-text(\"试验信息管理\")")

    # Click text=试验方案设置
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-plans"):
    with page.expect_navigation():
        page.click("text=试验方案设置")

    # Click text=试验项目设置
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items"):
    with page.expect_navigation():
        page.click("text=试验项目设置")

    # Click td:has-text("温升试验")
    # with page.expect_navigation(url="http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings"):
    with page.expect_navigation():
        arr = []
        # page.wait_for_function("""
        #     () => document.querySelector("span.ant-page-header-heading-title").innerText === '工位绑定'
        # """)
        page.wait_for_selector('.ant-table-body')
        table = page.query_selector('.ant-table-body')
        thead = table.query_selector_all('thead > tr > th')
        arr.append([th.query_selector('.ant-table-column-title').text_content() for th in thead[2:-1]])
        tbodyTrList = table.query_selector_all('tbody > tr')
        for tr in tbodyTrList:
            arr.append([th.text_content() for th in tr.query_selector_all('td')[2:-1]])
        print(arr)
        # 读取元素
        # print(await page.$("table"))
        # print(page.text_content("tr:nth-child(1) > td:nth-child(4)"));
        # print(page.text_content("tr:nth-child(2) > td:nth-child(3)"));
        # print(page.text_content("tr:nth-child(3) > td:nth-child(3)"));
    # Go to http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/test-info/test-items/39/test-station-bindings")

    #time.sleep(1000)
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
