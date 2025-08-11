def solve():
    """Index: 1221.
    Returns: the total number of ducks and ducklings.
    """
    # L1
    num_ducks_group1 = 2 # 2 ducks
    ducklings_per_duck_group1 = 5 # 5 ducklings each
    ducklings_group1 = num_ducks_group1 * ducklings_per_duck_group1

    # L2
    num_ducks_group2 = 6 # 6 ducks
    ducklings_per_duck_group2 = 3 # 3 ducklings each
    ducklings_group2 = num_ducks_group2 * ducklings_per_duck_group2

    # L3
    num_ducks_group3 = 9 # 9 ducks
    ducklings_per_duck_group3 = 6 # 6 ducklings each
    ducklings_group3 = num_ducks_group3 * ducklings_per_duck_group3

    # L4
    total_ducks_and_ducklings = ducklings_group1 + ducklings_group2 + ducklings_group3 + num_ducks_group1 + num_ducks_group2 + num_ducks_group3

    # FA
    answer = total_ducks_and_ducklings
    return answer