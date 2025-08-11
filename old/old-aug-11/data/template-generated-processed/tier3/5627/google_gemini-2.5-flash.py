def solve():
    """Index: 5627.
    Returns: the total number of errors fixed.
    """
    # L1
    total_lines_of_code = 4300 # 4300 lines of code
    debug_interval = 100 # Every 100 lines of code
    debug_times = total_lines_of_code / debug_interval

    # L2
    errors_per_debug = 3 # only finds three errors
    total_errors_fixed = debug_times * errors_per_debug

    # FA
    answer = total_errors_fixed
    return answer