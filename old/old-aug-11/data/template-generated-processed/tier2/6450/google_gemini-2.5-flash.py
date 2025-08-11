def solve():
    """Index: 6450.
    Returns: Trisha's annual "take-home" pay.
    """
    # L1
    hourly_rate = 15 # pays 15 dollars an hour
    hours_per_week = 40 # 40 hours per week
    weeks_per_year = 52 # 52 weeks in a year
    annual_gross_pay = hourly_rate * hours_per_week * weeks_per_year

    # L2
    withholding_percent_text = 20 # 20 percent
    withholding_rate_decimal = 0.2 # 0.2 x 31,200
    withheld_amount = withholding_rate_decimal * annual_gross_pay

    # L3
    annual_take_home_pay = annual_gross_pay - withheld_amount

    # FA
    answer = annual_take_home_pay
    return answer