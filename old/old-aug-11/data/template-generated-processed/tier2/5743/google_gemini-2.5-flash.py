def solve():
    """Index: 5743.
    Returns: the cost of Mark's new phone plan.
    """
    # L1
    old_plan_cost = 150 # old plan was $150 a month
    increase_percent_decimal = 0.3 # 30% more expensive
    cost_increase = old_plan_cost * increase_percent_decimal

    # L2
    new_plan_cost = old_plan_cost + cost_increase

    # FA
    answer = new_plan_cost
    return answer