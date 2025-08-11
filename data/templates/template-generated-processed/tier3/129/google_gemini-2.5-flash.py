def solve():
    """Index: 129.
    Returns: the number of free ice cream cones given away.
    """
    # L1
    total_sales = 100 # sold $100 worth of cones
    cone_cost = 2 # Cones cost $2 each
    cones_sold = total_sales / cone_cost

    # L2
    paid_cones_per_free_cone = 5 # every sixth customer gets a free ice cream cone (meaning 5 paid for 1 free)
    free_cones_given_away = cones_sold / paid_cones_per_free_cone

    # FA
    answer = free_cones_given_away
    return answer