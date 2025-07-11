def solve():
    """Index: 1812.
    Returns: the number of hours Bret has left to take a nap.
    """
    # L1
    train_ride_reading_hours = 2 # 2 hours reading a book
    train_ride_dinner_hours = 1 # 1 hour to eat his dinner
    train_ride_movies_hours = 3 # 3 hours watching movies on his computer
    total_activity_hours = train_ride_reading_hours + train_ride_dinner_hours + train_ride_movies_hours

    # L2
    total_train_ride_hours = 9 # 9 hour train ride
    hours_left_for_nap = total_train_ride_hours - total_activity_hours

    # FA
    answer = hours_left_for_nap
    return answer