def solve():
    """Index: 6665.
    Returns: the total amount of money Tom found in dollars.
    """
    # L1
    num_quarters = 10 # 10 quarters
    quarter_value = 0.25 # WK
    quarters_total_value = num_quarters * quarter_value

    # L2
    num_dimes = 3 # 3 dimes
    dime_value = 0.1 # WK
    dimes_total_value = num_dimes * dime_value

    # L3
    num_nickels = 4 # 4 nickels
    nickel_value = 0.05 # WK
    nickels_total_value = num_nickels * nickel_value

    # L4
    num_pennies = 200 # 200 pennies
    penny_value = 0.01 # WK
    pennies_total_value = num_pennies * penny_value

    # L5
    total_money_found = quarters_total_value + dimes_total_value + nickels_total_value + pennies_total_value

    # FA
    answer = total_money_found
    return answer