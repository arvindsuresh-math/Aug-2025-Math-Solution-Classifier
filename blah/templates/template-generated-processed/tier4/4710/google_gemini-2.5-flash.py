def solve():
    """Index: 4710.
    Returns: the distance from Missouri to New York by car.
    """
    # L1
    plane_distance_az_ny = 2000 # 2,000 miles by plane

    # L2
    increase_percent_num = 40 # increases by 40%
    percent_factor = 0.01 # WK
    increase_distance = increase_percent_num * percent_factor * plane_distance_az_ny

    # L3
    car_distance_az_ny = plane_distance_az_ny + increase_distance

    # L4
    midway_divisor = 2 # Missouri is midway
    distance_mo_ny = car_distance_az_ny / midway_divisor

    # FA
    answer = distance_mo_ny
    return answer