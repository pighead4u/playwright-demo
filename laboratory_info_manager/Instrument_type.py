# 仪器类型设置
# 测试仪器类型设置的增删改查
def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    print("Instrument_type_test_create start")
    page = context.new_page()
    _test_create(page)
    page.close()
    print("Instrument_type_test_create end")

    print("Instrument_type_test_rename start")
    page = context.new_page()
    _test_rename(page)
    page.close()
    print("Instrument_type_test_rename end")

    print("Instrument_type_test_delete start")
    page = context.new_page()
    _test_delete(page)
    page.close()
    print("Instrument_type_test_delete end")

    page.close()
    context.close()
    browser.close()

# 测试两种情况：
# 1、创建已经存在的仪器类型，创建失败
# 2、创建未存在的仪器类型，创建成功
def _test_create(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instrument-types")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "EMC")
    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "EMC试验系统")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instrument_types") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1,Exception("不存在相同名称的仪器类型！！！")
    # Click button:has-text("新增")
    page.click("button:has-text(\"新增\")")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "1234567")
    # Click button:has-text("确定")
    with page.expect_response("**/api/v1/instrument_types") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == '1234567',Exception("创建新的仪器类型失败！！！")

# 测试两种情况：
# 1、重命名已经存在的仪器类型，重命名失败
# 2、重命名未存在的仪器类型，重命名成功
def _test_rename(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instrument-types")
    # Click text=1234567重命名删除 >> button
    page.click("text=1234567重命名删除 >> button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "")
    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "EMC")
    # Press CapsLock
    page.press("[placeholder=\"请输入\"]", "CapsLock")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "EMC试验系统")
    with page.expect_response("**/api/v1/instrument_types/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['code'] == -1, Exception("不存在相同名称的仪器类型!!!")
    # Click text=1234567重命名删除 >> button
    page.click("text=1234567重命名删除 >> button")
    # Click [placeholder="请输入"]
    page.click("[placeholder=\"请输入\"]")
    # Fill [placeholder="请输入"]
    page.fill("[placeholder=\"请输入\"]", "123456789")
    with page.expect_response("**/api/v1/instrument_types/*") as response_info:
        page.click("button:has-text(\"确定\")")
        t = response_info.value.json()
        assert t['data']['name'] == '123456789', Exception("重命名仪器类型失败！！！")

# 测试删除功能：
def _test_delete(page):
    page.goto("http://mes-dev.tunnel.shunjiantech.cn/#/laboratory-info/instrument-types")
    page.click("text=123456789重命名删除 >> :nth-match(button, 2)")
    page.click("button:has-text(\"确定\")")
    with page.expect_response("**/api/v1/instrument_types/*") as response_info:
        t = response_info.value.json()
        assert t['code'] == 0,Exception("删除企仪器类型失败！！！")