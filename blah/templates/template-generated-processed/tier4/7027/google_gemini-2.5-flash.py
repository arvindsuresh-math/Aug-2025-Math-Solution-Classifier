def solve():
    """Index: 7027.
    Returns: the number of miles run on day three.
    """
    # L1
    total_miles = 70 # 70 miles
    day1_percent = 0.20 # 20 percent of the total miles
    day1_miles = total_miles * day1_percent

    # L2
    remaining_miles_after_day1 = total_miles - day1_miles

    # L3
    day2_divisor = 2 # 50 percent of the remaining miles
    day2_miles = remaining_miles_after_day1 / day2_divisor

    # L4
    remaining_miles_after_day2 = remaining_miles_after_day1 - day2_miles

    # FA
    answer = remaining_miles_after_day2
    return answer