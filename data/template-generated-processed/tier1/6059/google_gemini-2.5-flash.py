def solve():
    """Index: 6059.
    Returns: the total number of papers Kyle delivers each week.
    """
    # L1
    days_mon_to_sat = 6 # WK
    houses_daily_route = 100 # 100 houses on his route
    papers_mon_to_sat = days_mon_to_sat * houses_daily_route

    # L2
    sunday_customers_no_paper = 10 # 10 of his customers do not get the Sunday paper
    sunday_only_customers = 30 # delivers 30 papers to other houses that get the newspaper only on Sunday
    papers_sunday = houses_daily_route - sunday_customers_no_paper + sunday_only_customers

    # L3
    total_papers_per_week = papers_mon_to_sat + papers_sunday

    # FA
    answer = total_papers_per_week
    return answer