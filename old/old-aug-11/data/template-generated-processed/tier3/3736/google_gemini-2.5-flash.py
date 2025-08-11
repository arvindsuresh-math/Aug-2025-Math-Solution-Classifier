from fractions import Fraction

def solve():
    """Index: 3736.
    Returns: the total number of calories Jackson eats.
    """
    # L1
    lettuce_calories = 50 # 50 calories
    carrot_multiplier = 2 # twice the calories of the lettuce
    carrot_calories = lettuce_calories * carrot_multiplier

    # L2
    dressing_calories = 210 # 210 calories
    total_salad_calories = carrot_calories + lettuce_calories + dressing_calories

    # L3
    pepperoni_fraction = Fraction(1, 3) # 1/3 the crust's calories
    crust_calories = 600 # 600 calories for the crust
    pepperoni_calories = pepperoni_fraction * crust_calories

    # L4
    cheese_calories = 400 # 400 calories for the cheese
    total_pizza_calories = pepperoni_calories + crust_calories + cheese_calories

    # L5
    salad_portion = Fraction(1, 4) # 1/4 of the salad
    jackson_salad_calories = total_salad_calories * salad_portion

    # L6
    pizza_portion = Fraction(1, 5) # 1/5 of the pizza
    jackson_pizza_calories = total_pizza_calories * pizza_portion

    # L7
    total_calories_jackson_ate = jackson_salad_calories + jackson_pizza_calories

    # FA
    answer = total_calories_jackson_ate
    return answer