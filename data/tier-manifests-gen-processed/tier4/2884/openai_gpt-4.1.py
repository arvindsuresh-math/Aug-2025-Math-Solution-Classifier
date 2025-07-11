def solve():
    """Index: 2884.
    Returns: the number of pounds Felix can lift off the ground.
    """
    # L1
    brother_lift = 600 # his brother can lift 600 pounds
    brother_lift_factor = 3 # can lift three times his weight
    brother_weight = brother_lift / brother_lift_factor

    # L2
    brother_to_felix_weight_ratio = 2 # weighs twice as much as Felix
    felix_weight = brother_weight / brother_to_felix_weight_ratio

    # L3
    felix_lift_factor = 1.5 # Felix can lift off the ground 1.5 times more than he weighs
    felix_lift = felix_weight * felix_lift_factor

    # FA
    answer = felix_lift
    return answer