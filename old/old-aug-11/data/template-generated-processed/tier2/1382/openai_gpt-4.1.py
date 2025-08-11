def solve():
    """Index: 1382.
    Returns: the total amount you pay after the first year for the streaming service.
    """
    # L1
    monthly_subscription = 14 # subscription costs $14 a month
    split_percent_num = 50 # even split is 50%
    percent_factor = 0.01 # WK
    monthly_payment = monthly_subscription * split_percent_num * percent_factor

    # L2
    months_per_year = 12 # in 1 year there are 12 months
    total_payment = monthly_payment * months_per_year

    # FA
    answer = total_payment
    return answer