def solve():
    """Index: 482.
    Returns: the total number of calories Ian burns after 5 days.
    """
    # L1
    laps_per_night = 5 # He does 5 laps around the complex every night
    feet_per_lap = 100 # Each lap is 100 feet
    feet_per_day = laps_per_night * feet_per_lap

    # L2
    number_of_days = 5 # after 5 days of jogging like this
    total_feet_jogged = feet_per_day * number_of_days

    # L3
    feet_per_calorie = 25 # If it takes 25 feet of jogging to burn a calorie
    total_calories_burned = total_feet_jogged / feet_per_calorie

    # FA
    answer = total_calories_burned
    return answer