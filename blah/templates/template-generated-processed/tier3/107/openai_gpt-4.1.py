from fractions import Fraction

def solve():
    """Index: 107.
    Returns: the total number of cars traveling down Happy Street from Monday through Sunday.
    """
    # L1
    percent_less_monday = Fraction(20, 100) # 20% less than on Tuesday
    tuesday_cars = 25 # most cars pass it on Tuesday - 25
    monday_less_cars = percent_less_monday * tuesday_cars

    # L2
    monday_cars = tuesday_cars - monday_less_cars

    # L3
    wednesday_increment = 2 # 2 more cars than on Monday
    wednesday_cars = monday_cars + wednesday_increment

    # L4
    thursday_friday_cars_per_day = 10 # about 10 cars each day
    thursday_friday_days = 2 # Thursday and Friday
    thursday_friday_total = thursday_friday_cars_per_day * thursday_friday_days

    # L5
    weekend_cars_per_day = 5 # traffic drops to 5 cars per day
    weekend_days = 2 # weekend
    weekend_total = weekend_cars_per_day * weekend_days

    # L6
    total_cars = monday_cars + tuesday_cars + wednesday_cars + thursday_friday_total + weekend_total

    # FA
    answer = total_cars
    return answer