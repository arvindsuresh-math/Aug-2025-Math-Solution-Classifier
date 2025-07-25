def solve():
    """Index: 4838.
    Returns: the target kilos of newspaper.
    """
    # L1
    kilos_in_two_weeks = 280 # Each section collected 280 kilos in two weeks
    weeks_collected = 2 # in two weeks
    kilos_per_section_per_week = kilos_in_two_weeks / weeks_collected

    # L2
    total_weeks_collected = 3 # After the third week
    kilos_per_section_three_weeks = kilos_per_section_per_week * total_weeks_collected

    # L3
    sections_in_calculation = 4 # number of sections for total collection
    total_kilos_collected_by_sections = kilos_per_section_three_weeks * sections_in_calculation

    # L4
    kilos_needed_more = 320 # they need 320 kilos more
    target_kilos = total_kilos_collected_by_sections + kilos_needed_more

    # FA
    answer = target_kilos
    return answer