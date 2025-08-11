def solve():
    """Index: 1435.
    Returns: the total amount of money Harriett found.
    """
    # L1
    num_quarters = 10 # 10 quarters
    value_quarter = 0.25 # $0.25 each
    quarters_total = num_quarters * value_quarter

    # L2
    num_dimes = 3 # 3 dimes
    value_dime = 0.10 # $0.10 each
    dimes_total = num_dimes * value_dime

    # L3
    num_nickels = 3 # 3 nickels
    value_nickel = 0.05 # $0.05 each
    nickels_total = num_nickels * value_nickel

    # L4
    num_pennies = 5 # 5 pennies
    value_penny = 0.01 # $0.01 each
    pennies_total = num_pennies * value_penny

    # L5
    total_money = quarters_total + dimes_total + nickels_total + pennies_total

    # FA
    answer = total_money
    return answer