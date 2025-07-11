def solve():
    """Index: 1705.
    Returns: the total number of flowers Maria will have.
    """
    # L1
    num_dozens_bought = 3 # buy 3 dozens flowers
    free_flowers_per_dozen = 2 # gets 2 free flowers
    total_free_flowers = num_dozens_bought * free_flowers_per_dozen

    # L2
    dozen = 12 # WK
    total_bought_flowers = num_dozens_bought * dozen

    # L3
    total_flowers = total_bought_flowers + total_free_flowers

    # FA
    answer = total_flowers
    return answer