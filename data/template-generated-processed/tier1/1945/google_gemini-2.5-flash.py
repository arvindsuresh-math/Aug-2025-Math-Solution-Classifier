def solve():
    """Index: 1945.
    Returns: the number of pounds of apples Diego can buy.
    """
    # L1
    watermelon_weight = 1 # a pound of watermelon
    grapes_weight = 1 # a pound of grapes
    oranges_weight = 1 # a pound of oranges
    total_initial_fruit_weight = watermelon_weight + grapes_weight + oranges_weight

    # L2
    bookbag_capacity = 20 # 20 pounds of fruit
    apples_can_buy = bookbag_capacity - total_initial_fruit_weight

    # FA
    answer = apples_can_buy
    return answer