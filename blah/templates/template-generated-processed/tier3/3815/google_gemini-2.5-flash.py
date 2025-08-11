def solve():
    """Index: 3815.
    Returns: the number of additional miles Richard has to walk.
    """
    # L1
    first_day_miles = 20 # Richards walks 20 miles the first day
    less_miles = 6 # 6 miles less
    second_day_miles = first_day_miles / 2 - less_miles

    # L2
    third_day_miles = 10 # He walks 10 miles the third day
    total_miles_walked = first_day_miles + second_day_miles + third_day_miles

    # L3
    total_distance = 70 # which is 70 miles
    remaining_miles = total_distance - total_miles_walked

    # FA
    answer = remaining_miles
    return answer