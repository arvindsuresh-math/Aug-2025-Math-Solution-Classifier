def solve():
    """Index: 402.
    Returns: the profit the production company made from the movie.
    """
    # L1
    opening_weekend_gross = 120 # $120 million in the box office for its opening weekend
    total_run_multiplier = 3.5 # 3.5 times that much during its entire run
    total_gross_million = opening_weekend_gross * total_run_multiplier
    total_gross = total_gross_million * 1_000_000 # convert million to actual dollars, WK

    # L2
    production_company_percent = 0.6 # production company gets to keep 60%
    company_revenue = total_gross * production_company_percent

    # L3
    production_cost = 60_000_000 # movie cost $60 million to produce
    profit = company_revenue - production_cost

    # FA
    answer = profit
    return answer