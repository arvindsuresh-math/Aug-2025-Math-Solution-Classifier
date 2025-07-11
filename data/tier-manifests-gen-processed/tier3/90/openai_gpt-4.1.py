from fractions import Fraction

def solve():
    """Index: 90.
    Returns: the total number of cups of food Herman will need for all three months.
    """
    # L1
    december_days = 31 # December has 31 days
    january_days = 31 # January has 31 days
    february_days = 28 # February has 28 days
    total_days = december_days + january_days + february_days

    # L2
    morning_feed = Fraction(1, 2) # 1/2 cup in the morning
    afternoon_feed = Fraction(1, 2) # 1/2 cup in the afternoon
    cups_per_day = morning_feed + afternoon_feed

    # L3
    total_cups = cups_per_day * total_days

    # FA
    answer = total_cups
    return answer