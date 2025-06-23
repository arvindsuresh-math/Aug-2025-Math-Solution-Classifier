def solve(
    hourly_wage: int = 6, # Brendan makes $6/hour as a waiter
    num_8hr_shifts: int = 2, # scheduled for 2 8-hour shifts
    hours_per_8hr_shift: int = 8, # 8-hour shifts
    num_12hr_shifts: int = 1, # 1 12-hour shift
    hours_per_12hr_shift: int = 12, # 12-hour shift
    avg_tips_per_hour: int = 12, # average of $12 in tips each hour
    tax_rate: float = 0.2, # supposed to pay 20% of his income in taxes
    reported_tips_fraction: float = 1/3 # only reports 1/3rd of his tips to the IRS
):
    """Index: 6237.
    Returns: the amount Brendan pays in taxes each week.
    """
    #: L1
    total_8hr_shift_hours = num_8hr_shifts * hours_per_8hr_shift

    #: L2
    total_hours = total_8hr_shift_hours + (num_12hr_shifts * hours_per_12hr_shift)

    #: L3
    wage_earnings = hourly_wage * total_hours

    #: L4
    total_tips = avg_tips_per_hour * total_hours

    #: L5
    reported_tips = total_tips * reported_tips_fraction

    #: L6
    reported_income = wage_earnings + reported_tips

    #: L7
    taxes_paid = reported_income * tax_rate

    answer = taxes_paid # FINAL ANSWER
    return answer