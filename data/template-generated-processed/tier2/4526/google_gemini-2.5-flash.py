def solve():
    """Index: 4526.
    Returns: the total amount Tom will have to pay.
    """
    # L1
    cost_per_vaccine = 45 # each cost $45
    num_vaccines = 10 # 10 different vaccines
    doctors_visit_cost = 250 # doctor's visit costs $250
    total_medical_cost = cost_per_vaccine * num_vaccines + doctors_visit_cost

    # L2
    insurance_coverage_percent = 0.8 # cover 80% of these medical bills
    insurance_covered_amount = total_medical_cost * insurance_coverage_percent

    # L3
    out_of_pocket_medical_cost = total_medical_cost - insurance_covered_amount

    # L4
    trip_cost = 1200 # The trip itself cost $1200
    total_cost_to_pay = trip_cost + out_of_pocket_medical_cost

    # FA
    answer = total_cost_to_pay
    return answer