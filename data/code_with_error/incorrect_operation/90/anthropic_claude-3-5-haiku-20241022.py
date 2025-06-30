def solve(
        days_december: int = 31,  # December has 31 days
        days_january: int = 31,   # January has 31 days
        days_february: int = 28,  # February has 28 days
        morning_feed: float = 0.5,  # 1/2 cup in the morning
        afternoon_feed: float = 0.5  # 1/2 cup in the afternoon
    ):
    """Index: 90.
    Returns: the total number of cups of bird food needed for three months.
    """

    #: L1
    total_days = days_december + days_january + days_february

    #: L2
    daily_feed = morning_feed * afternoon_feed

    #: L3
    total_bird_food = daily_feed * total_days

    #: FA
    answer = total_bird_food
    return answer