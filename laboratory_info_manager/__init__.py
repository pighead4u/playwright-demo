from laboratory_info_manager import national_standard, Instrument_type, test_area, test_instrument


def run(playwright):
    national_standard.run(playwright)
    Instrument_type.run(playwright)
    test_area.run(playwright)
    test_instrument.run(playwright)
