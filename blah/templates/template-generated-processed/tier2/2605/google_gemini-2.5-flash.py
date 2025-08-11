def solve():
    """Index: 2605.
    Returns: the total amount John paid.
    """
    # L1
    cost_per_appointment = 400 # cost $400 each
    insurance_coverage_percent = 0.8 # covers 80% of the subsequent visits
    discount_per_visit = cost_per_appointment * insurance_coverage_percent

    # L2
    total_appointments = 3 # 3 vet appointments
    uncovered_appointments = 1 # After the first appointment
    num_covered_visits = total_appointments - uncovered_appointments

    # L3
    cost_per_covered_visit = cost_per_appointment - discount_per_visit

    # L4
    total_cost_covered_visits = num_covered_visits * cost_per_covered_visit

    # L5
    insurance_cost = 100 # paid $100 for pet insurance
    total_paid = cost_per_appointment + total_cost_covered_visits + insurance_cost

    # FA
    answer = total_paid
    return answer