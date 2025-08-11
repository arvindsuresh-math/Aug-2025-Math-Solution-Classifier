def solve():
    """Index: 515.
    Returns: the percentage chance of Annie getting into a serious accident if she drives.
    """
    # L1
    freezing_point = 32 # 32 degrees
    current_temp = 8 # 8 degrees
    degrees_below_freezing = freezing_point - current_temp

    # L2
    degrees_per_increase = 3 # every 3 degrees the temperature drops
    num_increases = degrees_below_freezing / degrees_per_increase

    # L3
    percent_increase_per = 5 # 5% increase
    total_skid_risk = num_increases * percent_increase_per

    # L4
    regain_control_chance = 40 # 40% of regaining control
    accident_after_skid_chance = 100 - regain_control_chance

    # L5
    # The chance of going into a skid is total_skid_risk (in percent), and the chance of a serious accident after a skid is accident_after_skid_chance (in percent).
    answer = (total_skid_risk / 100) * accident_after_skid_chance
    return answer