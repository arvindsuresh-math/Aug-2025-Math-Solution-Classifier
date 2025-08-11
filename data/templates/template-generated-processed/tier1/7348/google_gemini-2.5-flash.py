def solve():
    """Index: 7348.
    Returns: the total miles Amy biked in two days.
    """
    # L1
    yesterday_miles = 12 # Amy biked 12 miles yesterday
    multiplier_twice = 2 # Twice the distance
    twice_yesterday_miles = yesterday_miles * multiplier_twice

    # L2
    less_than_twice = 3 # 3 miles less than twice as far
    today_miles = twice_yesterday_miles - less_than_twice

    # L3
    total_miles = today_miles + yesterday_miles

    # FA
    answer = total_miles
    return answer