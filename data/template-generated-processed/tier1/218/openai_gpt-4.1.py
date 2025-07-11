def solve():
    """Index: 218.
    Returns: the total amount of money Ravi has in cents.
    """
    # L1
    num_nickels = 6 # he has 6 nickels
    quarters_more_than_nickels = 2 # 2 more quarters than nickels
    num_quarters = num_nickels + quarters_more_than_nickels

    # L2
    dimes_more_than_quarters = 4 # 4 more dimes than quarters
    num_dimes = num_quarters + dimes_more_than_quarters

    # L3
    value_nickel = 5 # WK
    value_nickels = num_nickels * value_nickel

    # L4
    value_quarter = 25 # WK
    value_quarters = num_quarters * value_quarter

    # L5
    value_dime = 10 # WK
    value_dimes = num_dimes * value_dime

    # L6
    total_cents = value_nickels + value_quarters + value_dimes

    # FA
    answer = total_cents
    return answer