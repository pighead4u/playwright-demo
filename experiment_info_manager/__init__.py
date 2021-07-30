from experiment_info_manager import requester, manufactory


def run(playwright):
    requester.run(playwright)
    manufactory.run(playwright)
