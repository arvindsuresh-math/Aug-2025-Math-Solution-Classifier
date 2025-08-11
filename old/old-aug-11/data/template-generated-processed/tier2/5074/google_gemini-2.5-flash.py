def solve():
    """Index: 5074.
    Returns: the total money Jerry makes from piercing noses and ears.
    """
    # L1
    nose_piercing_cost = 20 # $20 to pierce someone's nose
    ear_piercing_markup_percent = 50 # 50% more
    percent_to_decimal_factor = 0.01 # WK
    ear_piercing_markup_amount = nose_piercing_cost * ear_piercing_markup_percent * percent_to_decimal_factor

    # L2
    ear_piercing_cost = ear_piercing_markup_amount + nose_piercing_cost

    # L3
    num_ears_pierced = 9 # 9 ears
    total_ear_piercing_earnings = ear_piercing_cost * num_ears_pierced

    # L4
    num_noses_pierced = 6 # 6 noses
    total_nose_piercing_earnings = nose_piercing_cost * num_noses_pierced

    # L5
    total_income = total_nose_piercing_earnings + total_ear_piercing_earnings

    # FA
    answer = total_income
    return answer