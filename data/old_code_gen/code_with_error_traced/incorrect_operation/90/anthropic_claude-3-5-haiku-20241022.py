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
    total_days = days_december + days_january + days_february # eval: 90 = 31 + 31 + 28

    #: L2
    daily_feed = morning_feed * afternoon_feed # eval: 0.25 = 0.5 * 0.5

    #: L3
    total_bird_food = daily_feed * total_days # eval: 22.5 = 0.25 * 90

    #: FA
    answer = total_bird_food
    return answer # eval: return 22.5
