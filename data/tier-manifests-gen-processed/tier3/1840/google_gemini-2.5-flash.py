def solve():
    """Index: 1840.
    Returns: the number of nickels Ray has left.
    """
    # L1
    cents_given_to_peter = 25 # gives 25 cents to Peter
    randi_multiplier = 2 # twice as many cents to Randi
    cents_given_to_randi = cents_given_to_peter * randi_multiplier

    # L2
    initial_cents = 95 # Ray has 95 cents
    remaining_cents = initial_cents - cents_given_to_peter - cents_given_to_randi

    # L3
    nickel_value = 5 # WK
    remaining_nickels = remaining_cents / nickel_value

    # FA
    answer = remaining_nickels
    return answer