from experiment_info_manager import requester, manufactory, equipment_type, test_scheme, test_items


def run(playwright):
    requester.run(playwright)
    manufactory.run(playwright)
    equipment_type.run(playwright)
    test_items.run(playwright)
    test_scheme.run(playwright)
