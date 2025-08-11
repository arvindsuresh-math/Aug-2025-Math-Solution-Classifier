def solve():
    """Index: 4073.
    Returns: the total number of red apples Brogan gets.
    """
    # L1
    total_apples_per_tree = 20 # each produce 20 apples
    first_tree_red_percent_decimal = 0.4 # 40% red
    red_apples_first_tree = total_apples_per_tree * first_tree_red_percent_decimal

    # L2
    second_tree_red_percent_decimal = 0.5 # 50% red
    red_apples_second_tree = total_apples_per_tree * second_tree_red_percent_decimal

    # L3
    total_red_apples = red_apples_second_tree + red_apples_first_tree

    # FA
    answer = total_red_apples
    return answer