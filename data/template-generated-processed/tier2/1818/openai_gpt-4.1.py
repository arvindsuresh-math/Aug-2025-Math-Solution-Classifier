def solve():
    """Index: 1818.
    Returns: the number of non-hot peppers Joel picked.
    """
    # L1
    sunday_peppers = 7 # picks 7 on Sunday
    monday_peppers = 12 # 12 on Monday
    tuesday_peppers = 14 # 14 on Tuesday
    wednesday_peppers = 12 # 12 on Wednesday
    thursday_peppers = 5 # 5 on Thursday
    friday_peppers = 18 # 18 on Friday
    saturday_peppers = 12 # 12 on Saturday
    total_peppers = sunday_peppers + monday_peppers + tuesday_peppers + wednesday_peppers + thursday_peppers + friday_peppers + saturday_peppers

    # L2
    percent_total = 100 # WK
    percent_hot = 20 # 20% of the peppers are hot
    percent_non_hot = percent_total - percent_hot

    # L3
    percent_non_hot_decimal = 0.8 # 80% as decimal
    non_hot_peppers = total_peppers * percent_non_hot_decimal

    # FA
    answer = non_hot_peppers
    return answer