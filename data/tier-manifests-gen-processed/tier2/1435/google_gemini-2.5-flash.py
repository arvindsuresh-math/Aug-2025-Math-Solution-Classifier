def solve():
    """Index: 1435.
    Returns: the total amount of money Harriett found.
    """
    # L1
    num_quarters = 10 # 10 quarters
    value_quarter = 0.25 # WK
    total_quarters_value = num_quarters * value_quarter

    # L2
    num_dimes = 3 # 3 dimes
    value_dime = 0.10 # WK
    total_dimes_value = num_dimes * value_dime

    # L3
    num_nickels = 3 # 3 nickels
    value_nickel = 0.05 # WK
    total_nickels_value = num_nickels * value_nickel

    # L4
    num_pennies = 5 # 5 pennies
    value_penny = 0.01 # WK
    total_pennies_value = num_pennies * value_penny

    # L5
    total_money_found = total_quarters_value + total_dimes_value + total_nickels_value + total_pennies_value

    # FA
    answer = total_money_found
    return answer