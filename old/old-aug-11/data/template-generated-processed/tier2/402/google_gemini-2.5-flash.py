def solve():
    """Index: 402.
    Returns: the profit made by the production company.
    """
    # L1
    opening_weekend_revenue_million = 120 # $120 million in the box office
    total_run_multiplier = 3.5 # 3.5 times that much
    total_run_revenue_million = opening_weekend_revenue_million * total_run_multiplier

    # L2
    million_factor = 1000000 # WK
    total_revenue_full_amount = total_run_revenue_million * million_factor
    company_share_decimal = 0.6 # keep 60%
    company_revenue = total_revenue_full_amount * company_share_decimal

    # L3
    production_cost_million = 60 # movie cost $60 million to produce
    production_cost_full_amount = production_cost_million * million_factor
    profit = company_revenue - production_cost_full_amount

    # FA
    answer = profit
    return answer