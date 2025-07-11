def solve():
    """Index: 218.
    Returns: the total amount of money Ravi has in cents.
    """
    # L1
    nickels_count = 6 # 6 nickels
    more_quarters_than_nickels = 2 # 2 more quarters than nickels
    quarters_count = nickels_count + more_quarters_than_nickels

    # L2
    more_dimes_than_quarters = 4 # 4 more dimes than quarters
    dimes_count = quarters_count + more_dimes_than_quarters

    # L3
    nickel_value_cents = 5 # WK
    nickels_value_cents = nickels_count * nickel_value_cents

    # L4
    quarter_value_cents = 25 # WK
    quarters_value_cents = quarters_count * quarter_value_cents

    # L5
    dime_value_cents = 10 # WK
    dimes_value_cents = dimes_count * dime_value_cents

    # L6
    total_money_cents = nickels_value_cents + quarters_value_cents + dimes_value_cents

    # FA
    answer = total_money_cents
    return answer