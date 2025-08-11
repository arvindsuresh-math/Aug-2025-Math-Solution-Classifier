def solve():
    """Index: 5258.
    Returns: the total miles Jim runs during the 90 days.
    """
    # L1
    miles_per_day_phase1 = 5 # running 5 miles every day
    days_phase1 = 30 # for 30 days straight
    total_miles_phase1 = miles_per_day_phase1 * days_phase1

    # L2
    miles_per_day_phase2 = 10 # run 10 miles a day
    days_phase2 = 30 # for the next 30 days
    total_miles_phase2 = miles_per_day_phase2 * days_phase2

    # L3
    miles_per_day_phase3 = 20 # runs 20 miles a day
    days_phase3 = 30 # for 30 days straight
    total_miles_phase3 = miles_per_day_phase3 * days_phase3

    # L4
    total_miles_overall = total_miles_phase1 + total_miles_phase2 + total_miles_phase3

    # FA
    answer = total_miles_overall
    return answer