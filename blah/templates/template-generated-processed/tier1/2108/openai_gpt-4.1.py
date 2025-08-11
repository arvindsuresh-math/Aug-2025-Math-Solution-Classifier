def solve():
    """Index: 2108.
    Returns: the total quantity of apples Adam bought on the three days.
    """
    # L1
    monday_apples = 15 # Adam bought 15 apples on Monday
    tuesday_multiplier = 3 # 3 times that quantity
    tuesday_apples = tuesday_multiplier * monday_apples

    # L2
    wednesday_multiplier = 4 # 4 times the quantity he bought on Tuesday
    wednesday_apples = wednesday_multiplier * tuesday_apples

    # L3
    total_apples = monday_apples + tuesday_apples + wednesday_apples

    # FA
    answer = total_apples
    return answer