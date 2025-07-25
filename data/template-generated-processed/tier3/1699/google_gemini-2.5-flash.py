def solve():
    """Index: 1699.
    Returns: the number of pink and purple flowers each.
    """
    # L1
    red_multiplier = 2 # twice as many red flowers as orange
    orange_flowers = 10 # 10 orange flowers
    red_flowers = red_multiplier * orange_flowers

    # L2
    yellow_less_than_red = 5 # five fewer yellow flowers than red
    yellow_flowers = red_flowers - yellow_less_than_red

    # L3
    sum_red_orange_yellow = red_flowers + orange_flowers + yellow_flowers

    # L4
    total_flowers_in_garden = 105 # 105 flowers of various colors
    pink_purple_total = total_flowers_in_garden - sum_red_orange_yellow

    # L5
    number_of_pink_purple_colors = 2 # pink and purple flowers... they have the same amount
    pink_purple_each = pink_purple_total / number_of_pink_purple_colors

    # FA
    answer = pink_purple_each
    return answer