from playwright.sync_api import sync_playwright

import experiment_info_manager

if __name__ == '__main__':
    with sync_playwright() as playwright:
        experiment_info_manager.run(playwright)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
