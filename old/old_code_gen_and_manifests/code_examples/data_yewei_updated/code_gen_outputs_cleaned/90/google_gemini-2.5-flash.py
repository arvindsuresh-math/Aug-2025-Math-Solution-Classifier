def solve(
        morning_feed_cups: float = 0.5, # 1/2 cup in the morning
        afternoon_feed_cups: float = 0.5, # 1/2 cup in the afternoon
        december_days: int = 31, # December has 31 days
        january_days: int = 31, # January has 31 days
        february_days: int = 28 # February has 28 days
    ):
    """Index: 90.
    Returns: the total number of cups of food needed for all three months.
    """
    #: L1
    total_days = december_days + january_days + february_days

    #: L2
    cups_per_day = morning_feed_cups + afternoon_feed_cups

    #: L3
    total_cups_needed = cups_per_day * total_days

    answer = total_cups_needed # FINAL ANSWER
    return answer