def solve():
    """Index: 1277.
    Returns: the number of apples in each basket now.
    """
    # L1
    total_apples = 64 # Jane picked 64 apples
    num_baskets = 4 # sorted them into 4 different baskets
    apples_per_basket_initial = total_apples / num_baskets

    # L2
    apples_taken_per_basket = 3 # her sister took 3 apples from each of the baskets
    apples_per_basket_final = apples_per_basket_initial - apples_taken_per_basket

    # FA
    answer = apples_per_basket_final
    return answer