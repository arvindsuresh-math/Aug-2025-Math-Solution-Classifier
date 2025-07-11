def solve():
    """Index: 2605.
    Returns: the total amount John paid for the dog's vet appointments and insurance.
    """
    # L1
    vet_appointment_cost = 400 # vet appointments, which cost $400 each
    insurance_coverage_percent = 0.8 # covers 80% of the subsequent visits
    discount_per_visit = vet_appointment_cost * insurance_coverage_percent

    # L2
    total_appointments = 3 # requires 3 vet appointments
    first_appointment = 1 # After the first appointment
    discounted_appointments = total_appointments - first_appointment

    # L3
    cost_per_discounted_visit = vet_appointment_cost - discount_per_visit

    # L4
    total_discounted_visits_cost = discounted_appointments * cost_per_discounted_visit

    # L5
    insurance_cost = 100 # John paid $100 for pet insurance
    total_paid = vet_appointment_cost + total_discounted_visits_cost + insurance_cost

    # FA
    answer = total_paid
    return answer