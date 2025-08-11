def solve():
    """Index: 6132.
    Returns: the number of shares of stocks they can buy.
    """
    # L1
    wife_weekly_savings = 100 # $100 every week
    weeks_per_month = 4 # 4 weeks/month
    wife_monthly_savings = wife_weekly_savings * weeks_per_month

    # L2
    husband_monthly_savings = 225 # $225 every month
    total_monthly_savings = wife_monthly_savings + husband_monthly_savings

    # L3
    savings_duration_months = 4 # After 4 months
    total_savings_after_duration = total_monthly_savings * savings_duration_months

    # L4
    investment_fraction_denominator = 2 # half of their money
    amount_to_invest = total_savings_after_duration / investment_fraction_denominator

    # L5
    cost_per_share = 50 # Each share of stocks costs $50
    number_of_shares = amount_to_invest / cost_per_share

    # FA
    answer = number_of_shares
    return answer