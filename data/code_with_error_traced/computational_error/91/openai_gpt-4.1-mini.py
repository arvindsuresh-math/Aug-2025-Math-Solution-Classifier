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
    total_pay = daily_wage + bonus # eval: 100 = 80 + 20

    #: L3
    hourly_rate = 0.0 # eval: 0.0 = 0.0

    #: FA
    answer = hourly_rate
    return answer # eval: return 0.0
