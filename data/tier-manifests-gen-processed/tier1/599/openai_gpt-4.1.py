def solve():
    """Index: 599.
    Returns: the cost of the candy bar in cents.
    """
    # L1
    num_quarters = 4 # 4 quarters
    value_quarter = 25 # WK
    quarters_cents = num_quarters * value_quarter

    # L2
    num_dimes = 3 # 3 dimes
    value_dime = 10 # WK
    dimes_cents = num_dimes * value_dime

    # L3
    num_nickels = 1 # a nickel
    value_nickel = 5 # WK
    nickels_cents = num_nickels * value_nickel

    # L4
    total_paid = quarters_cents + dimes_cents + nickels_cents

    # L5
    change = 4 # 4 cents back in change
    candy_bar_cost = total_paid - change

    # FA
    answer = candy_bar_cost
    return answer