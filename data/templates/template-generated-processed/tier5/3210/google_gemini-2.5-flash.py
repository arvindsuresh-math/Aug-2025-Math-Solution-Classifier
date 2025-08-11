def solve():
    """Index: 3210.
    Returns: the number of phone chargers Anna has.
    """
    # L3
    # The problem states that laptop chargers (l) are five times more than phone chargers (p), so l = 5p.
    # The total chargers are 24, so l + p = 24.
    # Substituting l = 5p into l + p = 24 gives 5p + p = 24.
    # Combining like terms (5p + p) results in 6p.
    laptop_charger_multiplier = 5 # five times more laptop chargers
    phone_chargers_coefficient = laptop_charger_multiplier + 1 # Combining like terms (5p + p = 6p)
    total_chargers = 24 # 24 chargers total

    # L4
    phone_chargers = total_chargers / phone_chargers_coefficient # p = 24 / 6

    # FA
    answer = phone_chargers
    return answer