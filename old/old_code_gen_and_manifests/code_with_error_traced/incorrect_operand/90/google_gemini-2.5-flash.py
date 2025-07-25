def solve(
        morning_food_cups: float = 1/2, # 1/2 cup in the morning
        afternoon_food_cups: float = 1/2, # 1/2 cup in the afternoon
        december_days: int = 31, # December has 31 days
        january_days: int = 31, # January has 31 days
        february_days: int = 28 # February has 28 days
    ):
    """Index: 90.
    Returns: the total number of cups of food Herman will need for all three months.
    """

    #: L1
    total_days = december_days + january_days + february_days # eval: 90 = 31 + 31 + 28

    #: L2
    food_per_day = december_days + afternoon_food_cups # eval: 31.5 = 31 + 0.5

    #: L3
    total_food_needed = food_per_day * total_days # eval: 2835.0 = 31.5 * 90

    #: FA
    answer = total_food_needed
    return answer # eval: return 2835.0
