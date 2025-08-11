def solve():
    """Index: 1382.
    Returns: the total amount paid for the service after the first year.
    """
    # L1
    monthly_subscription_cost = 14 # $14 a month
    split_percent_text = 50 # 50%
    percent_factor = 0.01 # WK
    monthly_payment = monthly_subscription_cost * split_percent_text * percent_factor

    # L2
    months_per_year = 12 # in 1 year there are 12 months
    total_yearly_payment = monthly_payment * months_per_year

    # FA
    answer = total_yearly_payment
    return answer