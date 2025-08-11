def solve():
    """Index: 2370.
    Returns: how many more calories per hour Brandon gets if he catches squirrels instead of rabbits.
    """
    # L1
    calories_per_squirrel = 300 # Each squirrel has 300 calories
    squirrels_per_hour = 6 # can catch 6 squirrels in 1 hour
    squirrel_calories_per_hour = calories_per_squirrel * squirrels_per_hour

    # L2
    calories_per_rabbit = 800 # each rabbit has 800 calories
    rabbits_per_hour = 2 # can catch two rabbits in 1 hour
    rabbit_calories_per_hour = calories_per_rabbit * rabbits_per_hour

    # L3
    calorie_difference = squirrel_calories_per_hour - rabbit_calories_per_hour

    # FA
    answer = calorie_difference
    return answer