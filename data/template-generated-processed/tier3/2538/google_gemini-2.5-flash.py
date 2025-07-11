def solve():
    """Index: 2538.
    Returns: the number of more nickels Randi has than Peter.
    """
    # L1
    cents_given_to_peter = 30 # gives 30 cents to Peter
    randi_multiplier = 2 # twice as many cents to Randi
    cents_given_to_randi = cents_given_to_peter * randi_multiplier

    # L2
    nickel_value = 5 # WK
    randi_nickels = cents_given_to_randi / nickel_value

    # L3
    peter_nickels = cents_given_to_peter / nickel_value

    # L4
    difference_in_nickels = randi_nickels - peter_nickels

    # FA
    answer = difference_in_nickels
    return answer