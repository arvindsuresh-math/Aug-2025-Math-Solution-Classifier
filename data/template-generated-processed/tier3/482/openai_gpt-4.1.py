def solve():
    """Index: 482.
    Returns: the total number of calories Ian burns after 5 days of jogging.
    """
    # L1
    laps_per_day = 5 # does 5 laps around the complex every night
    feet_per_lap = 100 # Each lap is 100 feet
    feet_per_day = laps_per_day * feet_per_lap

    # L2
    days = 5 # after 5 days of jogging like this
    total_feet = feet_per_day * days

    # L3
    feet_per_calorie = 25 # it takes 25 feet of jogging to burn a calorie
    calories_burned = total_feet / feet_per_calorie

    # FA
    answer = calories_burned
    return answer