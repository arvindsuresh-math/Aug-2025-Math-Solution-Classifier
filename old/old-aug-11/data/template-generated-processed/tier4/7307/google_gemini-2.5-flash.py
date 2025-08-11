from fractions import Fraction

def solve():
    """Index: 7307.
    Returns: the total cost for Mark.
    """
    # L1
    weeks_of_food = 3 # enough food for 3 weeks
    days_per_week = 7 # WK
    total_days_food_needed = weeks_of_food * days_per_week

    # L2
    food_per_day = Fraction(1, 3) # puppy eats 1/3 cup of food a day
    total_cups_eaten = total_days_food_needed * food_per_day

    # L3
    cups_per_bag = 3.5 # A bag of food with 3.5 cups
    num_bags_needed = total_cups_eaten / cups_per_bag

    # L4
    cost_per_bag = 2 # costs $2
    total_food_cost = num_bags_needed * cost_per_bag

    # L5
    puppy_cost = 10 # puppy that cost $10
    total_overall_cost = puppy_cost + total_food_cost

    # FA
    answer = total_overall_cost
    return answer