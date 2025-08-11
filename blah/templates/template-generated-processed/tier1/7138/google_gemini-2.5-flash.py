def solve():
    """Index: 7138.
    Returns: the number of miles farther Henri drove.
    """
    # L1
    days_gervais_drove = 3 # 3 days
    gervais_avg_miles_per_day = 315 # average of 315 miles
    gervais_total_miles = days_gervais_drove * gervais_avg_miles_per_day

    # L2
    henri_total_miles = 1250 # total of 1,250 miles
    miles_farther = henri_total_miles - gervais_total_miles

    # FA
    answer = miles_farther
    return answer