def solve():
    """Index: 570.
    Returns: the total amount of money, in cents, put into the pond.
    """
    # L1
    value_dime_cents = 10 # WK
    cindy_dimes = 5 # 5 dimes
    cindy_total_cents = value_dime_cents * cindy_dimes

    # L2
    eric_quarters = 3 # 3 quarters
    value_quarter_cents = 25 # WK
    eric_initial_cents = eric_quarters * value_quarter_cents

    # L3
    garrick_nickels = 8 # 8 nickels
    value_nickel_cents = 5 # WK
    garrick_total_cents = garrick_nickels * value_nickel_cents

    # L4
    ivy_pennies = 60 # 60 pennies
    value_penny_cents = 1 # WK
    ivy_total_cents = ivy_pennies * value_penny_cents

    # L5
    eric_pulled_out_quarter_value = 25 # pulls out a quarter
    eric_remaining_cents = eric_initial_cents - eric_pulled_out_quarter_value

    # L6
    total_money_in_pond_cents = cindy_total_cents + eric_remaining_cents + garrick_total_cents + ivy_total_cents

    # FA
    answer = total_money_in_pond_cents
    return answer