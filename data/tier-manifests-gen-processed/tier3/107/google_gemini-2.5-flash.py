from fractions import Fraction

def solve():
    """Index: 107.
    Returns: the total number of cars that travel down Happy Street from Monday through Sunday.
    """
    # L1
    monday_less_percentage = Fraction(20, 100) # 20% less than on Tuesday
    tuesday_cars = 25 # Tuesday - 25
    cars_less_on_monday = monday_less_percentage * tuesday_cars

    # L2
    monday_cars = tuesday_cars - cars_less_on_monday

    # L3
    wednesday_additional_cars = 2 # 2 more cars than on Monday
    wednesday_cars = monday_cars + wednesday_additional_cars

    # L4
    cars_per_weekday_end = 10 # 10 cars each day
    num_days_thursday_friday = 2 # WK
    thursday_friday_cars = cars_per_weekday_end * num_days_thursday_friday

    # L5
    cars_per_weekend_day = 5 # traffic drops to 5 cars per day
    num_weekend_days = 2 # WK
    weekend_cars = cars_per_weekend_day * num_weekend_days

    # L6
    total_cars_week = monday_cars + tuesday_cars + wednesday_cars + thursday_friday_cars + weekend_cars

    # FA
    answer = total_cars_week
    return answer