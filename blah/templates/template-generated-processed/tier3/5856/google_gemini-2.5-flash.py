def solve():
    """Index: 5856.
    Returns: the total number of minutes Milly spends studying.
    """
    # L1
    math_homework_time = 60 # her math homework will take 60 minutes
    half_divisor = 2 # half as long
    geography_homework_time = math_homework_time / half_divisor

    # L2
    math_and_geography_total_time = geography_homework_time + math_homework_time

    # L3
    number_of_subjects_for_mean = 2 # the mean amount of time she spent studying math and geography
    science_homework_time = math_and_geography_total_time / number_of_subjects_for_mean

    # L4
    total_studying_time = science_homework_time + geography_homework_time + math_homework_time

    # FA
    answer = total_studying_time
    return answer