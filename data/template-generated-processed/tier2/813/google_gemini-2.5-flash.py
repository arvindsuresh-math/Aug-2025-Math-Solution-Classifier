def solve():
    """Index: 813.
    Returns: the amount of money Tom saved.
    """
    # L1
    normal_visit_cost = 200 # A normal doctor charges $200 for a visit
    discount_percent = 0.7 # 70% cheaper
    cheaper_amount_per_visit = normal_visit_cost * discount_percent

    # L2
    discount_visit_cost = normal_visit_cost - cheaper_amount_per_visit

    # L3
    num_discount_visits = 2 # It takes two visits
    total_discount_cost = discount_visit_cost * num_discount_visits

    # L4
    money_saved = normal_visit_cost - total_discount_cost

    # FA
    answer = money_saved
    return answer