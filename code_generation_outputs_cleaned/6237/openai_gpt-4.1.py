def solve(
    hourly_wage: int = 6,  # Brendan makes $6/hour as a waiter
    num_8hr_shifts: int = 2,  # He's scheduled for 2 8-hour shifts
    hours_per_8hr_shift: int = 8,  # Each 8-hour shift is 8 hours
    num_12hr_shifts: int = 1,  # 1 12-hour shift this week
    hours_per_12hr_shift: int = 12,  # Each 12-hour shift is 12 hours
    avg_tips_per_hour: int = 12,  # He also makes an average of $12 in tips each hour
    tax_rate: float = 0.2,  # Brendan is supposed to pay 20% of his income in taxes
    fraction_tips_reported: float = 1/3  # He only reports 1/3rd of his tips to the IRS
):
    """Code for Q 6237 from the GSM8K dataset (train).
    Returns the amount Brendan pays in taxes each week.
    """
    # First find the total number of hours Brendan works for the 8-hour shifts: 2 shifts * 8 hours/shift = <<2*8=16>>16 hours
    total_8hr_shift_hours = num_8hr_shifts * hours_per_8hr_shift

    # Then find the total number of hours Brendan works by adding those hours to the 12-hour shift: 16 hours + 12 hours = <<16+12=28>>28 hours
    total_hours = total_8hr_shift_hours + (num_12hr_shifts * hours_per_12hr_shift)

    # Now find Brendan's total wage earnings by multiplying his $6/hour wage by the number of hours he works: $6/hour * 28 hours = $<<6*28=168>>168/week
    wage_earnings = hourly_wage * total_hours

    # Now figure out how much Brendan makes in tips by multiplying the number of hours he works by the amount of tips he makes per hour: $12/hour * 28 hours/week = $<<12*28=336>>336/week
    total_tips = avg_tips_per_hour * total_hours

    # Now divide that number by 3, since Brendan only reports a third of his tips: $336/week / 3 = $<<336/3=112>>112/week
    reported_tips = total_tips * fraction_tips_reported

    # Now add Brendan's wage earnings to that number to find how much income he reports to the IRS each week: $168/week + $112/week = $<<168+112=280>>280/week
    reported_income = wage_earnings + reported_tips

    # Finally, multiply Brendan's reported income by his tax rate to find how much he pays in taxes each week: $280/week * .2 = $<<280*.2=56>>56/week
    taxes_paid = reported_income * tax_rate

    # The final answer is the amount Brendan pays in taxes each week
    return taxes_paid