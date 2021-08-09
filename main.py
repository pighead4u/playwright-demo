from playwright.sync_api import sync_playwright

import laboratory_info_manager
import experiment_info_manager
import receiving_or_returning
import system_setting

if __name__ == '__main__':
    with sync_playwright() as playwright:
        laboratory_info_manager.run(playwright)
        experiment_info_manager.run(playwright)
        receiving_or_returning.run(playwright)
        system_setting.run(playwright)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
