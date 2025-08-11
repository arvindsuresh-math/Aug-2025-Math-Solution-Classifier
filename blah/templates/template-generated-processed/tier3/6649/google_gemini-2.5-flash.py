def solve():
    """Index: 6649.
    Returns: the total number of steps Charlie was able to make.
    """
    # L1
    steps_per_3km = 5350 # 5350 steps
    full_runs = 2 # 2 1/2 times during a running session
    steps_for_full_runs = steps_per_3km * full_runs

    # L2
    half_run_divisor = 2 # 2 1/2 times during a running session
    steps_for_half_run = steps_per_3km / half_run_divisor

    # L3
    total_steps = steps_for_full_runs + steps_for_half_run

    # FA
    answer = total_steps
    return answer