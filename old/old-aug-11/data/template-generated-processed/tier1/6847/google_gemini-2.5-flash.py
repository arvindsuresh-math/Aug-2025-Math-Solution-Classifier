def solve():
    """Index: 6847.
    Returns: the total amount of pounds of food both sides are eating altogether every day.
    """
    # L1
    soldiers_side1 = 4000 # first side has 4000 soldiers
    food_per_soldier_side1 = 10 # needs 10 pounds of food every day
    food_side1 = soldiers_side1 * food_per_soldier_side1

    # L2
    soldiers_fewer_side2 = 500 # 500 soldiers fewer than the first side
    soldiers_side2 = soldiers_side1 - soldiers_fewer_side2

    # L3
    food_less_side2 = 2 # 2 pounds less food than the first side
    food_per_soldier_side2 = food_per_soldier_side1 - food_less_side2

    # L4
    food_side2 = food_per_soldier_side2 * soldiers_side2

    # L5
    total_food = food_side2 + food_side1

    # FA
    answer = total_food
    return answer