def solve():
    """Index: 3816.
    Returns: the total amount Goldie earned in two weeks for pet-sitting.
    """
    # L1
    hours_last_week = 20 # worked for 20 hours
    hours_this_week = 30 # worked for 30 hours
    total_hours_worked = hours_last_week + hours_this_week

    # L2
    hourly_rate = 5 # $5 an hour
    total_earnings = hourly_rate * total_hours_worked

    # FA
    answer = total_earnings
    return answer