from fractions import Fraction

def solve():
    """Index: 2311.
    Returns: the number of pounds of dog food left after a week.
    """
    # L1
    food_per_feeding = Fraction(1, 2) # 1/2 of a pound of dog food
    feedings_per_day = 2 # twice a day
    daily_food_per_dog = food_per_feeding * feedings_per_day

    # L2
    num_dogs = 3 # three dogs
    total_daily_food = daily_food_per_dog * num_dogs

    # L3
    days_per_week = 7 # WK
    weekly_food_consumption = total_daily_food * days_per_week

    # L4
    initial_food_bought = 30 # Melody bought 30 pounds of dog food
    food_left = initial_food_bought - weekly_food_consumption

    # FA
    answer = food_left
    return answer