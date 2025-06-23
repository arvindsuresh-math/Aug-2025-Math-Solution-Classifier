def solve(
    hourly_wage: int = 6, # Brendan makes $6/hour
    num_short_shifts: int = 2, # 2 8-hour shifts
    short_shift_hours: int = 8, # 2 8-hour shifts
    num_long_shifts: int = 1, # 1 12-hour shift
    long_shift_hours: int = 12, # 1 12-hour shift
    tips_per_hour: int = 12, # an average of $12 in tips each hour
    tax_rate: float = 0.20, # pay 20% of his income in taxes
    fraction_of_tips_reported: float = 1/3 # only reports 1/3rd of his tips
):
    """Index: 6237.
    Returns: the amount of money Brendan pays in taxes each week.
    """
    #: L1
    hours_from_short_shifts = num_short_shifts * short_shift_hours

    #: L2
    total_hours_worked = hours_from_short_shifts + long_shift_hours

    #: L3
    total_wage_earnings = hourly_wage * total_hours_worked

    #: L4
    total_tips = tips_per_hour * total_hours_worked

    #: L5
    reported_tips = total_tips / 3

    #: L6
    reported_income = total_wage_earnings + reported_tips

    #: L7
    taxes_paid = reported_income * tax_rate

    answer = taxes_paid # FINAL ANSWER
    return answer