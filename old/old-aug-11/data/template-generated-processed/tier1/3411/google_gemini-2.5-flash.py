def solve():
    """Index: 3411.
    Returns: the total time in seconds to complete the obstacle course.
    """
    # L1
    first_time_minutes = 7 # 7 minutes
    first_time_seconds_extra = 23 # 23 seconds
    seconds_per_minute = 60 # WK
    minutes_to_seconds_first_part = first_time_minutes * seconds_per_minute
    first_part_total_seconds = minutes_to_seconds_first_part + first_time_seconds_extra

    # L2
    second_stage_seconds = 73 # 73 seconds
    total_after_second_stage = second_stage_seconds + first_part_total_seconds

    # L3
    second_time_minutes = 5 # 5 minutes
    second_time_seconds_extra = 58 # 58 seconds
    minutes_to_seconds_second_part = second_time_minutes * seconds_per_minute
    second_part_total_seconds = minutes_to_seconds_second_part + second_time_seconds_extra

    # L4
    total_obstacle_course_time = total_after_second_stage + second_part_total_seconds

    # FA
    answer = total_obstacle_course_time
    return answer