def solve():
    """Index: 2369.
    Returns: the total cost for Eric to rent the house for 20 days.
    """
    # L1
    total_days = 20 # Eric wants to rent the house for 20 days
    deal_days = 14 # $500.00 for 14 days
    individual_days = total_days - deal_days

    # L2
    individual_day_rate = 50.00 # $50.00 per day
    individual_days_cost = individual_day_rate * individual_days

    # L3
    deal_cost = 500.00 # 14 days costs $500.00
    total_cost = deal_cost + individual_days_cost

    # FA
    answer = total_cost
    return answer