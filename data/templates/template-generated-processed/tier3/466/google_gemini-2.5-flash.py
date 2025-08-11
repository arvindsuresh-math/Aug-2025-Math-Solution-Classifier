def solve():
    """Index: 466.
    Returns: the total hours' worth of days Mark has left.
    """
    # L1
    sick_days = 10 # 10 sick days
    vacation_days = 10 # 10 vacation days
    total_allotment_days = sick_days + vacation_days

    # L2
    half_allotment_divisor = 2 # half his allotment
    remaining_days = total_allotment_days / half_allotment_divisor

    # L3
    hours_per_day = 8 # each day covers an 8-hour long workday
    remaining_hours = remaining_days * hours_per_day

    # FA
    answer = remaining_hours
    return answer