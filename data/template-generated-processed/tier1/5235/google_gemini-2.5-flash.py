def solve():
    """Index: 5235.
    Returns: how much more money Ms. Elizabeth made from her investments than Mr. Banks.
    """
    # L1
    mr_banks_investments_count = 8 # eight investments
    mr_banks_revenue_per_investment = 500 # $500 in revenue
    mr_banks_total_revenue = mr_banks_revenue_per_investment * mr_banks_investments_count

    # L2
    ms_elizabeth_revenue_per_investment = 900 # $900 from each of her 5 investment streams
    ms_elizabeth_investments_count = 5 # her 5 investment streams
    ms_elizabeth_total_revenue = ms_elizabeth_revenue_per_investment * ms_elizabeth_investments_count

    # L3
    difference_in_revenue = ms_elizabeth_total_revenue - mr_banks_total_revenue

    # FA
    answer = difference_in_revenue
    return answer