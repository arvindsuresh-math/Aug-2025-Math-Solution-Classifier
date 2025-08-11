def solve():
    """Index: 7149.
    Returns: the total amount spent on the newspaper over 8 weeks.
    """
    # L1
    num_weekday_papers = 3 # Wednesday, Thursday and Friday editions
    cost_weekday_paper = 0.50 # $0.50 each
    cost_weekday_papers_weekly = num_weekday_papers * cost_weekday_paper

    # L2
    cost_sunday_paper = 2.00 # $2.00 to get that copy
    total_weekly_cost = cost_weekday_papers_weekly + cost_sunday_paper

    # L3
    num_weeks = 8 # over 8 weeks
    total_cost_8_weeks = num_weeks * total_weekly_cost

    # FA
    answer = total_cost_8_weeks
    return answer