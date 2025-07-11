def solve():
    """Index: 2884.
    Returns: the amount Felix can lift off the ground.
    """
    # L1
    brother_lift_capacity = 600 # If his brother can lift 600 pounds
    brother_lift_multiple = 3 # can lift three times his weight
    brother_weight = brother_lift_capacity / brother_lift_multiple

    # L2
    brother_weight_multiple_felix = 2 # Felix's brother weighs twice as much as Felix
    felix_weight = brother_weight / brother_weight_multiple_felix

    # L3
    felix_lift_multiple = 1.5 # Felix can lift off the ground 1.5 times more than he weighs
    felix_lift_capacity = felix_weight * felix_lift_multiple

    # FA
    answer = felix_lift_capacity
    return answer