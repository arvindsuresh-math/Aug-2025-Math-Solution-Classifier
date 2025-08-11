def solve():
    """Index: 6808.
    Returns: the total number of oysters eaten by Crabby and Squido.
    """
    # L1
    squido_oysters = 200 # Squido eats 200 oysters
    crabby_multiplier = 2 # twice as many oysters
    crabby_oysters = crabby_multiplier * squido_oysters

    # L2
    total_oysters = crabby_oysters + squido_oysters

    # FA
    answer = total_oysters
    return answer