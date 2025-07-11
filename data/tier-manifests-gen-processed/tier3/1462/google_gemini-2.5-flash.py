def solve():
    """Index: 1462.
    Returns: the amount of food colouring each hard candy needs.
    """
    # L1
    ml_per_lollipop = 5 # Each lollipop uses 5ml of food colouring
    num_lollipops = 100 # makes 100 lollipops
    total_ml_for_lollipops = ml_per_lollipop * num_lollipops

    # L2
    total_food_colouring_used = 600 # used 600ml of food colouring
    total_ml_for_hard_candies = total_food_colouring_used - total_ml_for_lollipops

    # L3
    num_hard_candies = 5 # 5 hard candies
    ml_per_hard_candy = total_ml_for_hard_candies / num_hard_candies

    # FA
    answer = ml_per_hard_candy
    return answer