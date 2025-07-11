def solve():
    """Index: 685.
    Returns: the total number of kids in camp.
    """
    # L1
    afternoon_soccer_kids = 750 # 750 kids are going to soccer camp in the afternoon
    afternoon_fraction_numerator = 3 # 1/4 of the kids going to soccer camp are going to soccer camp in the morning. (implies 3/4 go in the afternoon)
    morning_soccer_kids = afternoon_soccer_kids / afternoon_fraction_numerator

    # L2
    total_soccer_camp_multiplier = 4 # 1/4 of the kids going to soccer camp
    total_soccer_camp_kids = morning_soccer_kids * total_soccer_camp_multiplier

    # L3
    total_camp_multiplier = 2 # Half of the kids are going to soccer camp
    total_kids_in_camp = total_soccer_camp_kids * total_camp_multiplier

    # FA
    answer = total_kids_in_camp
    return answer