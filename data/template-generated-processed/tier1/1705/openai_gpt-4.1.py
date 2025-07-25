def solve():
    """Index: 1705.
    Returns: the total number of flowers Maria will have in all.
    """
    # L1
    dozens_bought = 3 # Maria wants to buy 3 dozens flowers
    free_per_dozen = 2 # a customer gets 2 free flowers per dozen
    total_free = dozens_bought * free_per_dozen

    # L2
    dozen = 12 # WK
    bought_flowers = dozens_bought * dozen

    # L3
    total_flowers = bought_flowers + total_free

    # FA
    answer = total_flowers
    return answer