def solve():
    """Index: 4768.
    Returns: the total wait time for the vaccine doses.
    """
    # L1
    first_dose_wait_time = 20 # 20 minutes for the first dose
    half_divisor = 2 # half as long
    second_dose_wait_time = first_dose_wait_time / half_divisor

    # L2
    total_wait_time = first_dose_wait_time + second_dose_wait_time

    # FA
    answer = total_wait_time
    return answer