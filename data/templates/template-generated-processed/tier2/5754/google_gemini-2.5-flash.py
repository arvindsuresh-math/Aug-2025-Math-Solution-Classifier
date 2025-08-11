def solve():
    """Index: 5754.
    Returns: how far Alex had to walk.
    """
    # L1
    flat_speed = 20 # average speed over flat ground of about 20 miles per hour
    flat_duration = 4.5 # Four and a half hours later
    flat_distance = flat_speed * flat_duration

    # L2
    uphill_speed = 12 # only manage 12 miles per hour
    uphill_duration = 2.5 # Two and a half hours later
    uphill_distance = uphill_speed * uphill_duration

    # L3
    downhill_speed = 24 # mostly coast at 24 miles per hour
    downhill_duration = 1.5 # for one and a half hours
    downhill_distance = downhill_speed * downhill_duration

    # L4
    total_biked_distance = flat_distance + uphill_distance + downhill_distance

    # L5
    total_trip_distance = 164 # 164 miles from where he started this morning
    walk_distance = total_trip_distance - total_biked_distance

    # FA
    answer = walk_distance
    return answer