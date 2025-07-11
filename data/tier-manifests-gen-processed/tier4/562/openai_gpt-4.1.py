from fractions import Fraction

def solve():
    """Index: 562.
    Returns: the total cups of food Joy will need for the next 6 days.
    """
    # L1
    mom_cups_per_meal = 1.5 # The mom foster dog eats 1.5 cups of food
    mom_meals_per_day = 3 # three times a day
    mom_cups_per_day = mom_cups_per_meal * mom_meals_per_day

    # L2
    num_days = 6 # next 6 days
    mom_total_cups = num_days * mom_cups_per_day

    # L3
    puppy_cups_per_meal = Fraction(1, 2) # 1/2 cup of food
    puppy_meals_per_day = 2 # twice a day
    puppy_cups_per_day = puppy_cups_per_meal * puppy_meals_per_day

    # L4
    num_puppies = 5 # 5 puppies
    puppies_total_cups_per_day = num_puppies * puppy_cups_per_day

    # L5
    puppies_total_cups = puppies_total_cups_per_day * num_days

    # L6
    total_cups = mom_total_cups + puppies_total_cups

    # FA
    answer = total_cups
    return answer