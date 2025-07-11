def solve():
    """Index: 2370.
    Returns: the difference in calories Brandon gets per hour if he catches squirrels instead of rabbits.
    """
    # L1
    calories_per_squirrel = 300 # Each squirrel has 300 calories
    squirrels_caught_per_hour = 6 # catch 6 squirrels
    calories_from_squirrels_per_hour = calories_per_squirrel * squirrels_caught_per_hour

    # L2
    calories_per_rabbit = 800 # each rabbit has 800 calories
    rabbits_caught_per_hour = 2 # two rabbits
    calories_from_rabbits_per_hour = calories_per_rabbit * rabbits_caught_per_hour

    # L3
    calorie_difference = calories_from_squirrels_per_hour - calories_from_rabbits_per_hour

    # FA
    answer = calorie_difference
    return answer