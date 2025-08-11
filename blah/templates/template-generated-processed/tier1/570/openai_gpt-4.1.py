def solve():
    """Index: 570.
    Returns: the total amount of money, in cents, put into the pond.
    """
    # L1
    dime_value = 10 # value of a dime in cents, WK
    cindy_dimes = 5 # Cindy tosses 5 dimes
    cindy_cents = dime_value * cindy_dimes

    # L2
    eric_quarters = 3 # Eric flips 3 quarters
    quarter_value = 25 # value of a quarter in cents, WK
    eric_cents = eric_quarters * quarter_value

    # L3
    garrick_nickels = 8 # Garrick throws in 8 nickels
    nickel_value = 5 # value of a nickel in cents, WK
    garrick_cents = garrick_nickels * nickel_value

    # L4
    ivy_pennies = 60 # Ivy then drops 60 pennies
    penny_value = 1 # value of a penny in cents, WK
    ivy_cents = ivy_pennies * penny_value

    # L6
    total_cents = cindy_cents + eric_cents + garrick_cents + ivy_cents

    # FA
    answer = total_cents
    return answer