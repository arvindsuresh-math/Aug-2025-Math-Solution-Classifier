def solve():
    """Index: 4571.
    Returns: the total combined number of spots Granger and Cisco have.
    """
    # L1
    rover_spots = 46 # If Rover has 46 spots
    half_divisor = 2 # half as many spots
    half_rover_spots = rover_spots / half_divisor

    # L2
    less_than_half = 5 # 5 less than half as many spots
    cisco_spots = half_rover_spots - less_than_half

    # L3
    granger_multiplier = 5 # five times as many spots
    granger_spots = cisco_spots * granger_multiplier

    # L4
    total_granger_cisco_spots = granger_spots + cisco_spots

    # FA
    answer = total_granger_cisco_spots
    return answer