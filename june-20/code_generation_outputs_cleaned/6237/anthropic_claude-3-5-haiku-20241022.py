def solve(
        hourly_wage: float = 6,  # Brendan makes $6/hour as a waiter
        eight_hour_shifts: int = 2,  # He's scheduled for 2 8-hour shifts
        twelve_hour_shift: int = 1,  # and 1 12-hour shift
        tips_per_hour: float = 12,  # He makes an average of $12 in tips each hour
        tax_rate: float = 0.2,  # He is supposed to pay 20% of his income in taxes
        tips_reported_fraction: float = 1/3  # he only reports 1/3rd of his tips to the IRS
):
    """Index: 6237.
    Returns: the amount of taxes Brendan pays each week.
    """
    #: L1
    hours_from_eight_hour_shifts = eight_hour_shifts * 8

    #: L2
    total_hours_worked = hours_from_eight_hour_shifts + (twelve_hour_shift * 12)

    #: L3
    wage_earnings = hourly_wage * total_hours_worked

    #: L4
    total_tips = tips_per_hour * total_hours_worked

    #: L5
    reported_tips = total_tips * tips_reported_fraction

    #: L6
    reported_income = wage_earnings + reported_tips

    #: L7
    taxes_paid = reported_income * tax_rate

    answer = taxes_paid  # FINAL ANSWER
    return answer