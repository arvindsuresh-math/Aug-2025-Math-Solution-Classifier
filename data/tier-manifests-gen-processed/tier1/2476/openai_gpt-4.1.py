def solve():
    """Index: 2476.
    Returns: the total money Super Clean Car Wash Company will make in 5 days.
    """
    # L1
    cars_per_day = 80 # cleans 80 cars per day
    money_per_car = 5 # $5 per car washed
    daily_earnings = cars_per_day * money_per_car

    # L2
    num_days = 5 # in 5 days
    total_earnings = daily_earnings * num_days

    # FA
    answer = total_earnings
    return answer