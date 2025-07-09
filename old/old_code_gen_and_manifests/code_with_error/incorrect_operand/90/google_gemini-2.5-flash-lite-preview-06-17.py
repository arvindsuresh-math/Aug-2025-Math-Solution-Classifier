def solve(
    days_dec: int = 31, # December has 31 days
    days_jan: int = 31, # January has 31 days
    days_feb: int = 28, # February has 28 days
    morning_feed: float = 0.5, # He feeds them 1/2 cup in the morning
    afternoon_feed: float = 0.5 # and 1/2 cup in the afternoon
):
    """Index: 90.
    Returns: the total number of cups of food needed for all three months.
    """

    #: L1
    total_days = days_dec + days_jan + days_feb

    #: L2
    cups_per_day = morning_feed + afternoon_feed

    #: L3
    total_cups_needed = cups_per_day * days_feb

    #: FA
    answer = total_cups_needed
    return answer