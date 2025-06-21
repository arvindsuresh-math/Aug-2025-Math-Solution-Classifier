def solve(
    hourly_wage: int = 6,  # Brendan makes $6/hour as a waiter
    num_8hr_shifts: int = 2,  # He's scheduled for 2 8-hour shifts
    hours_per_8hr_shift: int = 8,  # each 8-hour shift
    num_12hr_shifts: int = 1,  # and 1 12-hour shift
    hours_per_12hr_shift: int = 12,  # each 12-hour shift
    tips_per_hour: int = 12,  # makes an average of $12 in tips each hour
    tax_rate: float = 0.2,  # Brendan is supposed to pay 20% of his income in taxes
    fraction_reported_tips: float = 1/3  # he only reports 1/3rd of his tips to the IRS
):
    """Index: 6237.
    Returns: the amount of money Brendan pays in taxes each week.
    """
    #: L1
    total_hours_8hr_shifts = num_8hr_shifts * hours_per_8hr_shift

    #: L2
    total_hours = total_hours_8hr_shifts + hours_per_12hr_shift

    #: L3
    total_wage_earnings = hourly_wage * total_hours

    #: L4
    total_tips = tips_per_hour * total_hours

    #: L5
    reported_tips = total_tips / 3

    #: L6
    reported_income = total_wage_earnings + reported_tips

    #: L7
    taxes_paid = reported_income * tax_rate

    answer = taxes_paid  # FINAL ANSWER
    return answer