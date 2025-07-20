def solve():
    """Index: 4825.
    Returns: the total number of minutes Arabella spent learning the three steps.
    """
    # L1
    first_step_time = 30 # thirty minutes on learning the first step
    half_time_divisor = 2 # half the time
    second_step_time = first_step_time / half_time_divisor

    # L2
    third_step_time = first_step_time + second_step_time

    # L3
    total_learning_time = first_step_time + second_step_time + third_step_time

    # FA
    answer = total_learning_time
    return answer