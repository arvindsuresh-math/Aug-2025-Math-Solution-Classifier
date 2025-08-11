def solve():
    """Index: 858.
    Returns: the number of candy bars Mark took.
    """
    # L1
    total_drink_calories = 2500 # contained 2500 calories
    sugar_percentage_drink_numerator = 5 # 5% of which was from added sugar
    percentage_denominator = 100 # WK
    sugar_from_drink = total_drink_calories * (sugar_percentage_drink_numerator / percentage_denominator)

    # L2
    recommended_intake = 150 # 150 calories of added sugar per day
    exceed_percentage_numerator = 100 # exceeded the recommended intake of added sugar by 100%
    total_sugar_consumed = recommended_intake + (recommended_intake * (exceed_percentage_numerator / percentage_denominator))

    # L3
    sugar_from_candy = total_sugar_consumed - sugar_from_drink

    # L4
    calories_per_bar = 25 # had 25 calories of added sugar each
    number_of_bars = sugar_from_candy / calories_per_bar

    # FA
    answer = number_of_bars
    return answer