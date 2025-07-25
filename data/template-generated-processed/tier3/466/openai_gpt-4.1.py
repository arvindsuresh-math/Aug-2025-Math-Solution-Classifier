def solve():
    """Index: 466.
    Returns: the number of hours' worth of days Mark has left.
    """
    # L1
    sick_days = 10 # each employee gets 10 sick days
    vacation_days = 10 # and 10 vacation days per year
    total_days = sick_days + vacation_days

    # L2
    used_fraction_denominator = 2 # uses half his allotment
    remaining_days = total_days / used_fraction_denominator

    # L3
    hours_per_day = 8 # each day covers an 8-hour long workday
    remaining_hours = remaining_days * hours_per_day

    # FA
    answer = remaining_hours
    return answer