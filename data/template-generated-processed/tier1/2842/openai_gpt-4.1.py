def solve():
    """Index: 2842.
    Returns: the total number of math problems Rachel did in all.
    """
    # L1
    problems_per_minute = 5 # Rachel solved 5 math problems each minute
    minutes_before_bed = 12 # for 12 minutes before bed
    problems_before_bed = problems_per_minute * minutes_before_bed

    # L2
    problems_at_lunch = 16 # she finished the last 16 problems at lunch
    total_problems = problems_before_bed + problems_at_lunch

    # FA
    answer = total_problems
    return answer