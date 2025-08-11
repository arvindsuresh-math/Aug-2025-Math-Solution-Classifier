def solve():
    """Index: 3322.
    Returns: the speed of the fifth coaster.
    """
    # L1
    average_speed = 59 # His average speed during the day was 59 miles per hour
    num_coasters = 5 # Tony goes on 5 rollercoasters
    total_speed_all_coasters = average_speed * num_coasters

    # L2
    speed_coaster1 = 50 # The first went 50 miles per hour
    speed_coaster2 = 62 # The second went 62 miles per hour
    speed_coaster3 = 73 # The third when 73 miles per hour
    speed_coaster4 = 70 # The fourth when 70 miles per hour
    speed_coaster5 = total_speed_all_coasters - speed_coaster1 - speed_coaster2 - speed_coaster3 - speed_coaster4

    # FA
    answer = speed_coaster5
    return answer