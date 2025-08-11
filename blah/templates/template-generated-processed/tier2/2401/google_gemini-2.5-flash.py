def solve():
    """Index: 2401.
    Returns: how far away from the zoo the tiger was caught.
    """
    # L1
    notice_time = 4 # zookeepers do not notice he is missing until 4 AM
    escape_time = 1 # escapes at 1 AM
    initial_run_duration = notice_time - escape_time

    # L2
    fast_speed = 25 # runs at a speed of 25 mph
    distance_before_notice = initial_run_duration * fast_speed

    # L3
    time_before_slow = 4 # after 4 hours of running
    additional_fast_run_duration = time_before_slow - initial_run_duration

    # L4
    additional_fast_distance = additional_fast_run_duration * fast_speed

    # L5
    slow_run_duration = 1 # It takes 2 more hours to find him (second hour of finding)
    slow_speed = 10 # the tiger slows his speed to 10 mph
    slow_distance = slow_run_duration * slow_speed

    # L6
    chase_speed = 50 # going 50 mph
    chase_duration = 0.5 # for half an hour
    chase_distance = chase_speed * chase_duration

    # L7
    total_distance = distance_before_notice + additional_fast_distance + slow_distance + chase_distance

    # FA
    answer = total_distance
    return answer