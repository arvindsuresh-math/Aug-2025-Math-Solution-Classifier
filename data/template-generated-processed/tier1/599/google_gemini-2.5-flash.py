def solve():
    """Index: 599.
    Returns: the cost of the candy bar in cents.
    """
    # L1
    num_quarters = 4 # 4 quarters
    cents_per_quarter = 25 # WK
    cents_from_quarters = num_quarters * cents_per_quarter

    # L2
    num_dimes = 3 # 3 dimes
    cents_per_dime = 10 # WK
    cents_from_dimes = num_dimes * cents_per_dime

    # L3
    num_nickels = 1 # a nickel
    cents_per_nickel = 5 # WK
    cents_from_nickel = cents_per_nickel * num_nickels

    # L4
    total_paid = cents_from_quarters + cents_from_dimes + cents_from_nickel

    # L5
    change_received = 4 # 4 cents back in change
    cost_of_candy_bar = total_paid - change_received

    # FA
    answer = cost_of_candy_bar
    return answer