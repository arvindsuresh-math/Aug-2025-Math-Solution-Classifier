from fractions import Fraction

def solve():
    """Index: 90.
    Returns: the total cups of food needed.
    """
    # L1
    december_days = 31 # WK
    january_days = 31 # WK
    february_days = 28 # WK
    total_days = december_days + january_days + february_days

    # L2
    morning_feed = Fraction(1, 2) # 1/2 cup in the morning
    afternoon_feed = Fraction(1, 2) # 1/2 cup in the afternoon
    daily_feed = morning_feed + afternoon_feed

    # L3
    total_food_needed = daily_feed * total_days

    # FA
    answer = total_food_needed
    return answer