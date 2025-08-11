def solve():
    """Index: 4046.
    Returns: the total hours Sam spent on tutoring for two months.
    """
    # L1
    first_month_earnings = 200 # For the first month, he earned $200
    additional_earnings_second_month = 150 # earned $150 more than the first month
    second_month_earnings = first_month_earnings + additional_earnings_second_month

    # L2
    total_earnings_two_months = first_month_earnings + second_month_earnings

    # L3
    hourly_rate = 10 # Sam earns $10 an hour
    total_hours = total_earnings_two_months / hourly_rate

    # FA
    answer = total_hours
    return answer