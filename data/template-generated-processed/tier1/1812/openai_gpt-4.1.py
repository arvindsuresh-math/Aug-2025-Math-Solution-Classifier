def solve():
    """Index: 1812.
    Returns: the number of hours Bret has left to take a nap.
    """
    # L1
    reading_hours = 2 # spends 2 hours reading a book
    dinner_hours = 1 # 1 hour to eat his dinner
    movies_hours = 3 # 3 hours watching movies on his computer
    total_activity_hours = reading_hours + dinner_hours + movies_hours

    # L2
    total_ride_hours = 9 # 9 hour train ride
    nap_hours = total_ride_hours - total_activity_hours

    # FA
    answer = nap_hours
    return answer