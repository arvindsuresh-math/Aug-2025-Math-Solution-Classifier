def solve():
    """Index: 1283.
    Returns: the difference in earnings between the two types of work.
    """
    # L1
    first_work_tasks = 400 # 400 work tasks
    first_work_rate = 0.25 # $0.25 each
    first_work_earnings = first_work_tasks * first_work_rate

    # L2
    second_work_tasks = 5 # 5 work tasks
    second_work_rate = 2.00 # $2.00 each
    second_work_earnings = second_work_tasks * second_work_rate

    # L3
    earnings_difference = first_work_earnings - second_work_earnings

    # FA
    answer = earnings_difference
    return answer