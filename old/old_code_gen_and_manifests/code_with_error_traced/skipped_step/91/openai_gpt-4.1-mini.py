def solve(
    daily_wage: int = 80,  # He makes $80 a day
    daily_hours: int = 8,  # works for 8 hours
    bonus: int = 20,       # performance bonus of an extra $20 a day
    extra_hours: int = 2   # extra effort results in a 2-hour longer workday
):
    """Index: 91.
    Returns: John's hourly wage if he decides to earn the bonus.
    """

    #: L1
    total_hours = daily_hours + extra_hours # eval: 10 = 8 + 2

    #: L2

    #: L3
    hourly_rate = bonus / total_hours # eval: 2.0 = 20 / 10

    #: FA
    answer = hourly_rate
    return answer # eval: return 2.0
