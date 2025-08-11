def solve():
    """Index: 6350.
    Returns: the difference in pizza rolls eaten by Tyler and Jackson.
    """
    # L1
    jackson_pizza_rolls = 10 # Jackson ate 10 pizza rolls
    jerome_factor = 2 # twice that amount
    jerome_pizza_rolls = jerome_factor * jackson_pizza_rolls

    # L2
    tyler_factor = 1.5 # one and half times more
    tyler_pizza_rolls = tyler_factor * jerome_pizza_rolls

    # L3
    difference_tyler_jackson = tyler_pizza_rolls - jackson_pizza_rolls

    # FA
    answer = difference_tyler_jackson
    return answer