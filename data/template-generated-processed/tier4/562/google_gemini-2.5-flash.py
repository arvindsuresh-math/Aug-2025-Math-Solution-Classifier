from fractions import Fraction

def solve():
    """Index: 562.
    Returns: the total amount of food Joy will need for the next 6 days.
    """
    # L1
    mom_food_per_meal = 1.5 # 1.5 cups of food
    mom_meals_per_day = 3 # three times a day
    mom_food_per_day = mom_food_per_meal * mom_meals_per_day

    # L2
    num_days = 6 # next 6 days
    mom_total_food = num_days * mom_food_per_day

    # L3
    puppy_food_per_meal = Fraction(1, 2) # 1/2 cup of food
    puppy_meals_per_day = 2 # twice a day
    puppy_food_per_puppy_per_day = puppy_food_per_meal * puppy_meals_per_day

    # L4
    num_puppies = 5 # 5 puppies
    puppies_total_food_per_day = num_puppies * puppy_food_per_puppy_per_day

    # L5
    puppies_total_food = puppies_total_food_per_day * num_days

    # L6
    total_food_needed = mom_total_food + puppies_total_food

    # FA
    answer = total_food_needed
    return answer