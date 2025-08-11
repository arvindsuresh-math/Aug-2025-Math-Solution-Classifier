def solve():
    """Index: 3041.
    Returns: the number of miles Wendy drove on the third day.
    """
    # L1
    miles_day1 = 125 # 125 miles on the first day
    miles_day2 = 223 # 223 miles on the second day
    miles_first_two_days = miles_day1 + miles_day2

    # L2
    total_miles_trip = 493 # total miles that Wendy drove for the trip is 493 miles
    miles_day3 = total_miles_trip - miles_first_two_days

    # FA
    answer = miles_day3
    return answer