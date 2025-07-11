def solve():
    """Index: 944.
    Returns: the number of daisies Kylie has left.
    """
    # L1
    initial_daisies = 5 # Kylie has 5 daisies
    given_daisies = 9 # Her sister gave her another 9 daisies
    total_daisies = initial_daisies + given_daisies

    # L2
    divisor = 2 # gave half her daisies
    remaining_daisies = total_daisies / divisor

    # FA
    answer = remaining_daisies
    return answer