def solve():
    """Index: 4723.
    Returns: Cary's net calorie deficit.
    """
    # L1
    miles_walked = 3 # 3 miles round-trip
    calories_per_mile = 150 # burns 150 calories per mile walked
    calories_burned_walking = miles_walked * calories_per_mile

    # L2
    calories_eaten = 200 # candy bar with 200 calories
    net_calorie_deficit = calories_burned_walking - calories_eaten

    # FA
    answer = net_calorie_deficit
    return answer