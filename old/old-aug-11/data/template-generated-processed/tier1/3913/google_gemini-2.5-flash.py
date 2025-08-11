def solve():
    """Index: 3913.
    Returns: the amount saved per year if choosing 20 Mbps over 30 Mbps.
    """
    # L1
    current_monthly_bill = 20 # her current monthly bill is $20
    multiplier_30mbps = 2 # twice the amount of her current monthly bill
    monthly_bill_30mbps = current_monthly_bill * multiplier_30mbps

    # L2
    months_per_year = 12 # WK
    annual_bill_30mbps = monthly_bill_30mbps * months_per_year

    # L3
    additional_cost_20mbps = 10 # $10 more than her current monthly bill
    monthly_bill_20mbps = current_monthly_bill + additional_cost_20mbps

    # L4
    annual_bill_20mbps = monthly_bill_20mbps * months_per_year

    # L5
    annual_savings = annual_bill_30mbps - annual_bill_20mbps

    # FA
    answer = annual_savings
    return answer