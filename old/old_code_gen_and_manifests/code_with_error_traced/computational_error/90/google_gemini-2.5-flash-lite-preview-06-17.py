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
    total_days = days_dec + days_jan + days_feb # eval: 90 = 31 + 31 + 28

    #: L2
    cups_per_day = 0.0 # eval: 0.0 = 0.0

    #: L3
    total_cups_needed = cups_per_day * total_days # eval: 0.0 = 0.0 * 90

    #: FA
    answer = total_cups_needed
    return answer # eval: return 0.0
