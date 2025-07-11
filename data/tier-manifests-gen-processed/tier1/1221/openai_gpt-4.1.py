def solve():
    """Index: 1221.
    Returns: the total number of ducks and ducklings.
    """
    # L1
    ducks1 = 2 # 2 ducks with 5 ducklings each
    ducklings_per_duck1 = 5 # 5 ducklings each
    ducklings1 = ducks1 * ducklings_per_duck1

    # L2
    ducks2 = 6 # 6 ducks with 3 ducklings each
    ducklings_per_duck2 = 3 # 3 ducklings each
    ducklings2 = ducks2 * ducklings_per_duck2

    # L3
    ducks3 = 9 # 9 ducks with 6 ducklings each
    ducklings_per_duck3 = 6 # 6 ducklings each
    ducklings3 = ducks3 * ducklings_per_duck3

    # L4
    total = ducklings1 + ducklings2 + ducklings3 + ducks1 + ducks2 + ducks3

    # FA
    answer = total
    return answer