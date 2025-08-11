def solve():
    """Index: 5959.
    Returns: the total number of pastries Lola and Lulu made.
    """
    # L1
    lola_mini_cupcakes = 13 # 13 mini cupcakes
    lulu_mini_cupcakes = 16 # 16 mini cupcakes
    total_mini_cupcakes = lola_mini_cupcakes + lulu_mini_cupcakes

    # L2
    lola_pop_tarts = 10 # 10 pop tarts
    lulu_pop_tarts = 12 # 12 pop tarts
    total_pop_tarts = lola_pop_tarts + lulu_pop_tarts

    # L3
    lola_blueberry_pies = 8 # 8 blueberry pies
    lulu_blueberry_pies = 14 # 14 blueberry pies
    total_blueberry_pies = lola_blueberry_pies + lulu_blueberry_pies

    # L4
    total_pastries = total_mini_cupcakes + total_pop_tarts + total_blueberry_pies

    # FA
    answer = total_pastries
    return answer