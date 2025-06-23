def solve(
        hourly_wage: int = 6, # Brendan makes $6/hour
        num_8hr_shifts: int = 2, # 2 8-hour shifts
        hours_per_8hr_shift: int = 8, # 8-hour shifts
        num_12hr_shifts: int = 1, # 1 12-hour shift
        hours_per_12hr_shift: int = 12, # 12-hour shift
        hourly_tips: int = 12, # $12 in tips each hour
        tax_rate: float = 0.2, # 20% of his income in taxes
        reported_tips_fraction: float = 1/3 # only reports 1/3rd of his tips
    ):
    """Index: 6237.
    Returns: the amount of money Brendan pays in taxes each week.
    """
    #: L1
    hours_8hr_shifts = num_8hr_shifts * hours_per_8hr_shift

    #: L2
    total_hours_worked = hours_8hr_shifts + hours_per_12hr_shift

    #: L3
    total_wage_earnings = hourly_wage * total_hours_worked

    #: L4
    total_tips_earned = hourly_tips * total_hours_worked

    #: L5
    reported_tips = total_tips_earned * reported_tips_fraction

    #: L6
    total_reported_income = total_wage_earnings + reported_tips

    #: L7
    taxes_paid = total_reported_income * tax_rate

    answer = taxes_paid # FINAL ANSWER
    return answer