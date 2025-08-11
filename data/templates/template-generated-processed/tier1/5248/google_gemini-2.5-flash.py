def solve():
    """Index: 5248.
    Returns: the total weight John can now lift.
    """
    # L1
    initial_squat_weight = 135 # squat 135 pounds
    increased_weight = 265 # increased that by 265 pounds
    weight_without_bracer = initial_squat_weight + increased_weight

    # L2
    strength_increase_percentage = 600 # increases his strength by an additional 600%
    strength_increase_multiplier = strength_increase_percentage / 100
    bracer_added_weight = weight_without_bracer * strength_increase_multiplier

    # L3
    total_lift_with_bracer = bracer_added_weight + weight_without_bracer

    # FA
    answer = total_lift_with_bracer
    return answer