def solve():
    """Index: 6615.
    Returns: the total amount Pete and Raymond spent altogether, in cents.
    """
    # L1
    pete_nickels_spent = 4 # spends 4 nickels
    nickel_value_cents = 5 # WK
    pete_spent_cents = pete_nickels_spent * nickel_value_cents

    # L2
    raymond_dimes_left = 7 # has 7 dimes left
    dime_value_cents = 10 # WK
    raymond_left_cents = raymond_dimes_left * dime_value_cents

    # L3
    initial_money_dollars = 2.50 # $2.50 from their grandmother
    initial_money_cents = int(initial_money_dollars * 100) # Convert dollars to cents
    raymond_spent_cents = initial_money_cents - raymond_left_cents

    # L4
    total_spent_cents = pete_spent_cents + raymond_spent_cents

    # FA
    answer = total_spent_cents
    return answer