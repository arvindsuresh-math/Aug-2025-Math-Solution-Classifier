def solve():
    """Index: 6499.
    Returns: Tricia's age in years.
    """
    # L1
    vincent_age = 22 # Vincent who is 22 years old
    rupert_age_difference_from_vincent = 2 # 2 years younger than Vincent
    rupert_age = vincent_age - rupert_age_difference_from_vincent

    # L2
    khloe_age_difference_from_rupert = 10 # 10 years older than Khloe
    khloe_age = rupert_age - khloe_age_difference_from_rupert

    # L3
    eugene_age_multiplier_from_khloe = 3 # Khloe is a third of Eugene's age
    eugene_age = khloe_age * eugene_age_multiplier_from_khloe

    # L4
    yorick_age_multiplier_from_eugene = 2 # Yorick is twice Eugene’s age
    yorick_age = eugene_age * yorick_age_multiplier_from_eugene

    # L5
    amilia_age_divisor_from_yorick = 4 # Amilia is a quarter of Yorick’s age
    amilia_age = yorick_age / amilia_age_divisor_from_yorick

    # L6
    tricia_age_divisor_from_amilia = 3 # Tricia is a third of Amilia’s age
    tricia_age = amilia_age / tricia_age_divisor_from_amilia

    # FA
    answer = tricia_age
    return answer