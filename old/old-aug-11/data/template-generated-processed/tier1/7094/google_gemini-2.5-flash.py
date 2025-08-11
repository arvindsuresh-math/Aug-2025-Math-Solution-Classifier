def solve():
    """Index: 7094.
    Returns: the total number of miles Molly rode on her bike.
    """
    # L1
    end_age = 16 # until she turned 16
    start_age = 13 # thirteenth birthday
    years_ridden = end_age - start_age

    # L2
    days_per_year = 365 # WK
    total_days_ridden = years_ridden * days_per_year

    # L3
    miles_per_day = 3 # 3 miles a day
    total_miles_ridden = miles_per_day * total_days_ridden

    # FA
    answer = total_miles_ridden
    return answer