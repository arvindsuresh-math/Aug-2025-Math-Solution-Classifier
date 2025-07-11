def solve():
    """Index: 813.
    Returns: the amount of money Tom saves by going to the discount clinic.
    """
    # L1
    normal_doctor_fee = 200 # A normal doctor charges $200 for a visit
    discount_percent = 0.7 # 70% cheaper
    per_visit_savings = normal_doctor_fee * discount_percent

    # L2
    per_visit_cost = normal_doctor_fee - per_visit_savings

    # L3
    num_visits = 2 # It takes two visits
    total_paid = per_visit_cost * num_visits

    # L4
    total_savings = normal_doctor_fee - total_paid

    # FA
    answer = total_savings
    return answer