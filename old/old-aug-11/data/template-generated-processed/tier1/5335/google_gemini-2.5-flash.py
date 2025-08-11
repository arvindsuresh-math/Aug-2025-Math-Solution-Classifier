def solve():
    """Index: 5335.
    Returns: the difference in money given on Thursday and Tuesday.
    """
    # L1
    money_tuesday = 8 # $8 dollars for a hot dog
    multiplier_wednesday = 5 # 5 times as much money
    money_wednesday = money_tuesday * multiplier_wednesday

    # L2
    extra_thursday = 9 # $9 more in money
    money_thursday = money_wednesday + extra_thursday

    # L3
    difference_thursday_tuesday = money_thursday - money_tuesday

    # FA
    answer = difference_thursday_tuesday
    return answer