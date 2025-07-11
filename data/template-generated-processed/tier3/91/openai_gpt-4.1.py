def solve():
    """Index: 91.
    Returns: John's hourly wage if he decides to earn the bonus.
    """
    # L1
    base_hours = 8 # works for 8 hours
    bonus_hours = 2 # extra effort results in a 2-hour longer workday
    total_hours = base_hours + bonus_hours

    # L2
    base_pay = 80 # makes $80 a day
    bonus_pay = 20 # performance bonus of an extra $20 a day
    total_pay = base_pay + bonus_pay

    # L3
    hourly_rate = total_pay / total_hours

    # FA
    answer = hourly_rate
    return answer