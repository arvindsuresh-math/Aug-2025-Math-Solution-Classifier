def solve():
    """Index: 5163.
    Returns: the total cups of food Rollo needs for all his Guinea pigs.
    """
    # L1
    first_guinea_pig_food = 2 # first guinea pig eats 2 cups of food
    multiplier_twice = 2 # twice as much as the first one
    second_guinea_pig_food = first_guinea_pig_food * multiplier_twice

    # L2
    third_guinea_pig_extra_food = 3 # 3 cups more than the second one
    third_guinea_pig_food = second_guinea_pig_food + third_guinea_pig_extra_food

    # L3
    total_food = first_guinea_pig_food + second_guinea_pig_food + third_guinea_pig_food

    # FA
    answer = total_food
    return answer