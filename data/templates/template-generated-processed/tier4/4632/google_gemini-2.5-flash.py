def solve():
    """Index: 4632.
    Returns: the amount each person should pay in tips.
    """
    # L1
    julie_food_cost = 10 # Julie orders $10 worth of food
    letitia_food_cost = 20 # Letitia orders $20 worth of food
    anton_food_cost = 30 # Anton orders $30 worth of food
    total_food_cost = julie_food_cost + letitia_food_cost + anton_food_cost

    # L2
    tip_percentage = 0.2 # 20% tip
    total_tip = total_food_cost * tip_percentage

    # L3
    num_people = 3 # three people
    tip_per_person = total_tip / num_people

    # FA
    answer = tip_per_person
    return answer