def solve():
    """Index: 2476.
    Returns: the total money the car wash company will make in 5 days.
    """
    # L1
    cars_per_day = 80 # cleans 80 cars per day
    money_per_car = 5 # $5 per car washed
    money_per_day = cars_per_day * money_per_car

    # L2
    num_days = 5 # in 5 days
    total_money = money_per_day * num_days

    # FA
    answer = total_money
    return answer