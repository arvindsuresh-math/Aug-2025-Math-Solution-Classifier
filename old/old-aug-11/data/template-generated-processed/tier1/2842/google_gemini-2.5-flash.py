def solve():
    """Index: 2842.
    Returns: the total number of math problems Rachel did.
    """
    # L1
    problems_per_minute = 5 # 5 math problems each minute
    minutes_before_bed = 12 # for 12 minutes before bed
    problems_before_bed = problems_per_minute * minutes_before_bed

    # L2
    problems_next_day = 16 # finished the last 16 problems
    total_problems = problems_before_bed + problems_next_day

    # FA
    answer = total_problems
    return answer