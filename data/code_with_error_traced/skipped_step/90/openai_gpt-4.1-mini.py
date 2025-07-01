def solve(
    days_december: int = 31,  # December has 31 days
    days_january: int = 31,   # January has 31 days
    days_february: int = 28,  # February has 28 days
    morning_cups: float = 0.5,  # feeds 1/2 cup in the morning
    afternoon_cups: float = 0.5  # feeds 1/2 cup in the afternoon
):
    """Index: 90.
    Returns: the total cups of bird food needed for December, January, and February.
    """

    #: L1
    total_days = days_december + days_january + days_february # eval: 90 = 31 + 31 + 28

    #: L2

    #: L3
    total_cups = morning_cups * total_days # eval: 45.0 = 0.5 * 90

    #: FA
    answer = total_cups
    return answer # eval: return 45.0
