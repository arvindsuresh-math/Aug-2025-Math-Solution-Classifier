def solve():
    """Index: 2705.
    Returns: the total monthly bill working from home.
    """
    # L1
    original_bill = 60 # $60 per month
    increase_percent_decimal = 0.30 # increased by thirty percent
    additional_cost = original_bill * increase_percent_decimal

    # L2
    total_monthly_bill = original_bill + additional_cost

    # FA
    answer = total_monthly_bill
    return answer