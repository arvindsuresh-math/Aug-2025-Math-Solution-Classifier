def solve():
    """Index: 5311.
    Returns: the total number of treats the children get.
    """
    # L1
    hours_out = 4 # out for 4 hours
    houses_per_hour = 5 # visited 5 houses
    total_houses_visited = hours_out * houses_per_hour

    # L2
    treats_per_kid_per_house = 3 # 3 treats per kid
    treats_per_child = total_houses_visited * treats_per_kid_per_house

    # L3
    num_children = 3 # 3 children
    total_treats = treats_per_child * num_children

    # FA
    answer = total_treats
    return answer