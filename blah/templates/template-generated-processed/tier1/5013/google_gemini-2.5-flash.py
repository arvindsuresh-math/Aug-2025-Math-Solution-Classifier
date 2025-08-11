def solve():
    """Index: 5013.
    Returns: the number of staplers left in the stapler.
    """
    # L1
    num_dozen_reports = 3 # 3 dozen reports
    dozen = 12 # WK
    reports_stapled = num_dozen_reports * dozen

    # L2
    initial_staplers = 50 # 50 staplers in the stapler
    staplers_left = initial_staplers - reports_stapled

    # FA
    answer = staplers_left
    return answer