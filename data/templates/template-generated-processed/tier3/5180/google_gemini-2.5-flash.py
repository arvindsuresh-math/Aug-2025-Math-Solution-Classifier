def solve():
    """Index: 5180.
    Returns: the number of kids going to soccer camp in the afternoon.
    """
    # L1
    total_kids_in_camp = 2000 # 2,000 kids in camp
    half_divisor = 2 # half of the kids
    kids_going_to_soccer_camp = total_kids_in_camp / half_divisor

    # L2
    morning_camp_denominator = 4 # 1/4 of the kids going to soccer camp
    kids_soccer_morning = kids_going_to_soccer_camp / morning_camp_denominator

    # L3
    afternoon_fraction_numerator = 3 # WK
    kids_soccer_afternoon = kids_soccer_morning * afternoon_fraction_numerator

    # FA
    answer = kids_soccer_afternoon
    return answer