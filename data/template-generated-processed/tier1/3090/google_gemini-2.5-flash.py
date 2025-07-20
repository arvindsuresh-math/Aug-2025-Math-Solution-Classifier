def solve():
    """Index: 3090.
    Returns: the maximum weight of a robot in the competition.
    """
    # L1
    standard_robot_weight = 100 # The standard robot weighs 100 pounds.
    min_weight_increase = 5 # 5 pounds heavier than the standard robot
    minimum_weight = standard_robot_weight + min_weight_increase

    # L2
    max_weight_multiplier = 2 # no more than twice the minimum weight
    maximum_weight = minimum_weight * max_weight_multiplier

    # FA
    answer = maximum_weight
    return answer