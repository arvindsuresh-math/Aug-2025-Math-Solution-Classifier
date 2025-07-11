def solve():
    """Index: 207.
    Returns: the total number of hours John volunteers per year.
    """
    # L1
    times_per_month = 2 # twice a month
    months_per_year = 12 # WK
    times_per_year = times_per_month * months_per_year

    # L2
    hours_per_time = 3 # 3 hours at a time
    total_hours = times_per_year * hours_per_time

    # FA
    answer = total_hours
    return answer