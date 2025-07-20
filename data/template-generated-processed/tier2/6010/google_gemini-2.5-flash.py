def solve():
    """Index: 6010.
    Returns: the total weight James can move with lifting straps for 10 meters.
    """
    # L1
    initial_lift_capacity = 300 # 300 pounds per hand
    increase_without_straps = 50 # increases his 20-meter distance without straps by 50 pounds
    lift_after_initial_increase = initial_lift_capacity + increase_without_straps

    # L2
    distance_increase_percent = 0.3 # lift 30% more
    lift_increase_from_distance = lift_after_initial_increase * distance_increase_percent

    # L3
    lift_for_10_meters = lift_after_initial_increase + lift_increase_from_distance

    # L4
    straps_increase_percent = 0.2 # another 20%
    lift_increase_from_straps = lift_for_10_meters * straps_increase_percent

    # L5
    total_lift_capacity = lift_for_10_meters + lift_increase_from_straps

    # FA
    answer = total_lift_capacity
    return answer