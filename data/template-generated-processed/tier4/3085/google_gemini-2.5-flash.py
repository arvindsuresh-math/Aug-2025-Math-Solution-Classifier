def solve():
    """Index: 3085.
    Returns: the total amount of money Caden has in dollars.
    """
    # L1
    pennies_count = 120 # 120 pennies
    penny_value = 0.01 # WK
    pennies_value_dollars = pennies_count * penny_value

    # L2
    pennies_per_nickel_ratio = 3 # three times as many pennies as he does nickels
    nickels_count = pennies_count / pennies_per_nickel_ratio
    nickel_value = 0.05 # WK
    nickels_value_dollars = nickels_count * nickel_value

    # L3
    nickels_per_dime_ratio = 5 # five times as many nickels as he does dimes
    dimes_count = nickels_count / nickels_per_dime_ratio
    dime_value = 0.10 # WK
    dimes_value_dollars = dimes_count * dime_value

    # L4
    quarters_per_dime_ratio = 2 # twice as many quarters as he does dimes
    quarters_count = dimes_count * quarters_per_dime_ratio
    quarter_value = 0.25 # WK
    quarters_value_dollars = quarters_count * quarter_value

    # L5
    total_money = pennies_value_dollars + nickels_value_dollars + dimes_value_dollars + quarters_value_dollars

    # FA
    answer = total_money
    return answer