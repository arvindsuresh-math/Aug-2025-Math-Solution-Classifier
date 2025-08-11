def solve():
    """Index: 2108.
    Returns: the total quantity of apples Adam bought on the three days.
    """
    # L1
    apples_monday = 15 # 15 apples on Monday
    tuesday_multiplier = 3 # 3 times that quantity
    apples_tuesday = tuesday_multiplier * apples_monday

    # L2
    wednesday_multiplier = 4 # 4 times the quantity he bought on Tuesday
    apples_wednesday = wednesday_multiplier * apples_tuesday

    # L3
    total_apples = apples_monday + apples_tuesday + apples_wednesday

    # FA
    answer = total_apples
    return answer