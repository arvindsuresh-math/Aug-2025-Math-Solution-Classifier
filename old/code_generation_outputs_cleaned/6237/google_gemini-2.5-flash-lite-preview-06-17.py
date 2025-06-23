def solve(
    hourly_wage: int = 6, # Brendan makes $6/hour as a waiter
    num_shifts_8_hour: int = 2, # He's scheduled for 2 8-hour shifts
    hours_per_8_hour_shift: int = 8, # He's scheduled for 2 8-hour shifts
    hours_per_12_hour_shift: int = 12, # and 1 12-hour shift this week
    avg_tips_per_hour: int = 12, # He also makes an average of $12 in tips each hour
    tax_rate: float = 0.2, # Brendan is supposed to pay 20% of his income in taxes
    tips_reported_fraction: float = 1/3 # but he only reports 1/3rd of his tips to the IRS
):
    """Code for Q 6237 from the GSM8K dataset (train).
    Returns the amount of money Brendan pays in taxes each week."""
    # First find the total number of hours Brendan works for the 8-hour shifts: 2 shifts * 8 hours/shift = <<2*8=16>>16 hours
    hours_from_8_hour_shifts = num_shifts_8_hour * hours_per_8_hour_shift

    # Then find the total number of hours Brendan works by adding those hours to the 12-hour shift: 16 hours + 12 hours = <<16+12=28>>28 hours
    total_hours_worked = hours_from_8_hour_shifts + hours_per_12_hour_shift

    # Now find Brendan's total wage earnings by multiplying his $6/hour wage by the number of hours he works: $6/hour * 28 hours = $<<6*28=168>>168/week
    total_wage_earnings = hourly_wage * total_hours_worked

    # Now figure out how much Brendan makes in tips by multiplying the number of hours he works by the amount of tips he makes per hour: $12/hour * 28 hours/week = $<<12*28=336>>336/week
    total_tips_earned = avg_tips_per_hour * total_hours_worked

    # Now divide that number by 3, since Brendan only reports a third of his tips: $336/week / 3 = $<<336/3=112>>112/week
    reported_tips = total_tips_earned * tips_reported_fraction

    # Now add Brendan's wage earnings to that number to find how much income he reports to the IRS each week: $168/week + $112/week = $<<168+112=280>>280/week
    total_reported_income = total_wage_earnings + reported_tips

    # Finally, multiply Brendan's reported income by his tax rate to find how much he pays in taxes each week: $280/week * .2 = $<<280*.2=56>>56/week
    taxes_paid = total_reported_income * tax_rate

    # The final answer is the amount of money Brendan pays in taxes each week
    return taxes_paid