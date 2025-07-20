def solve():
    """Index: 5473.
    Returns: the total amount of money Jill made over three months.
    """
    # L1
    days_per_month = 30 # assuming each month is 30 days long
    daily_rate_month1 = 10 # makes $10 a day for her first month
    earnings_month1 = days_per_month * daily_rate_month1

    # L2
    multiplier_month2 = 2 # double that per day
    earnings_month2 = multiplier_month2 * earnings_month1

    # L3
    work_frequency_divisor_month3 = 2 # only works every other day
    earnings_month3 = earnings_month2 / work_frequency_divisor_month3

    # L4
    total_earnings = earnings_month1 + earnings_month3 + earnings_month2

    # FA
    answer = total_earnings
    return answer