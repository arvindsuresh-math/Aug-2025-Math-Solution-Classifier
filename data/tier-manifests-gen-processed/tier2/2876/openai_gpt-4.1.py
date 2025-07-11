def solve():
    """Index: 2876.
    Returns: the total amount Aaron will owe his dad including interest.
    """
    # L1
    monthly_payment = 100 # $100.00 per month
    num_months = 12 # 12 months
    guitar_cost = monthly_payment * num_months

    # L2
    interest_rate_decimal = 0.10 # .10*1200
    interest_amount = guitar_cost * interest_rate_decimal

    # L3
    total_owed = guitar_cost + interest_amount

    # FA
    answer = total_owed
    return answer