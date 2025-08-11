def solve():
    """Index: 4459.
    Returns: the number of nickels Kendall has.
    """
    # L1
    num_quarters = 10 # 10 quarters
    value_per_quarter = 0.25 # WK
    total_money_quarters = num_quarters * value_per_quarter

    # L2
    num_dimes = 12 # 12 dimes
    value_per_dime = 0.10 # WK
    total_money_dimes = num_dimes * value_per_dime

    # L3
    total_money_all_coins = 4 # total of $4
    total_money_nickels = total_money_all_coins - total_money_quarters - total_money_dimes

    # L4
    value_per_nickel = 0.05 # WK
    num_nickels = total_money_nickels / value_per_nickel

    # FA
    answer = num_nickels
    return answer