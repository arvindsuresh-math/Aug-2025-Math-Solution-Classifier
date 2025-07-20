def solve():
    """Index: 4024.
    Returns: the total miles Jodi has walked in 4 weeks.
    """
    # L1
    miles_week1 = 1 # 1 mile a day
    days_per_week = 6 # 6 days a week
    total_miles_week1 = miles_week1 * days_per_week

    # L2
    miles_week2 = 2 # 2 miles a day
    total_miles_week2 = miles_week2 * days_per_week

    # L3
    miles_week3 = 3 # 3 miles a day
    total_miles_week3 = miles_week3 * days_per_week

    # L4
    miles_week4 = 4 # 4 miles a day
    total_miles_week4 = miles_week4 * days_per_week

    # L5
    total_miles_four_weeks = total_miles_week1 + total_miles_week2 + total_miles_week3 + total_miles_week4

    # FA
    answer = total_miles_four_weeks
    return answer