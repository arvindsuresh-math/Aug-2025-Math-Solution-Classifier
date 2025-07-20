def solve():
    """Index: 4064.
    Returns: the cost of a dozen chocolate bars.
    """
    # L1
    magazine_cost_per_unit = 1 # one magazine costs $1
    num_magazines_equal_to_chocolate = 8 # cost of 8 magazines
    cost_of_8_magazines = num_magazines_equal_to_chocolate * magazine_cost_per_unit

    # L4
    num_chocolate_bars_equal_to_magazines = 4 # cost of four chocolate bars
    cost_per_chocolate_bar = cost_of_8_magazines / num_chocolate_bars_equal_to_magazines

    # L5
    dozen = 12 # WK
    cost_of_dozen_chocolate_bars = dozen * cost_per_chocolate_bar

    # FA
    answer = cost_of_dozen_chocolate_bars
    return answer