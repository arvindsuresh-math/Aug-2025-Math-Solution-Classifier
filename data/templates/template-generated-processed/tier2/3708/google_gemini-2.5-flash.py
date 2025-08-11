def solve():
    """Index: 3708.
    Returns: the total length of time Rudy runs.
    """
    # L1
    first_run_miles = 5 # runs 5 miles
    first_run_rate = 10 # at a rate of 10 minutes per mile
    first_run_duration = first_run_miles * first_run_rate

    # L2
    second_run_miles = 4 # runs 4 miles
    second_run_rate = 9.5 # at a rate of 9.5 minutes per mile
    second_run_duration = second_run_miles * second_run_rate

    # L3
    total_run_duration = first_run_duration + second_run_duration

    # FA
    answer = total_run_duration
    return answer