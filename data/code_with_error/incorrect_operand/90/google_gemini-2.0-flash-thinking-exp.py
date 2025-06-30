def solve(
    morning_feeding_cups: float = 1/2, # He feeds them 1/2 cup in the morning
    afternoon_feeding_cups: float = 1/2, # and 1/2 cup in the afternoon
    december_days: int = 31, # December has 31 days
    january_days: int = 31, # January has 31 days
    february_days: int = 28 # and February has 28 days
):
    """Index: 90.
    Returns: the total number of cups of food needed for all three months.
    """

    #: L1
    total_days = december_days + january_days + february_days

    #: L2
    cups_per_day = morning_feeding_cups + december_days

    #: L3
    total_cups_needed = cups_per_day * total_days

    #: FA
    answer = total_cups_needed
    return answer