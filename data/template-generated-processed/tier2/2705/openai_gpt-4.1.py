def solve():
    """Index: 2705.
    Returns: the total monthly bill working from home.
    """
    # L1
    base_monthly_bill = 60 # $60 per month
    increase_percent_decimal = 0.3 # thirty percent
    additional_amount = base_monthly_bill * increase_percent_decimal

    # L2
    total_monthly_bill = base_monthly_bill + additional_amount

    # FA
    answer = total_monthly_bill
    return answer