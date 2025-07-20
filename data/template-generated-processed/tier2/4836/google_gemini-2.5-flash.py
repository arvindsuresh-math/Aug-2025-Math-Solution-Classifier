def solve():
    """Index: 4836.
    Returns: the total dollars Jon makes in a 30 day month.
    """
    # L1
    visits_per_hour = 50 # 50 visits
    paid_per_visit = 0.10 # $0.10 for every person who visits
    earnings_per_hour = visits_per_hour * paid_per_visit

    # L2
    hours_per_day = 24 # 24 hours a day
    earnings_per_day = earnings_per_hour * hours_per_day

    # L3
    days_per_month = 30 # 30 day month
    earnings_per_month = earnings_per_day * days_per_month

    # FA
    answer = earnings_per_month
    return answer