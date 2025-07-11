def solve():
    """Index: 153.
    Returns: the total amount Tim paid for his and his cat's visits.
    """
    # L1
    doctor_visit_cost = 300 # His doctor's visits $300
    insurance_coverage_percent = 0.75 # insurance covered 75%
    insurance_covered_amount = doctor_visit_cost * insurance_coverage_percent

    # L2
    paid_for_doctor_visit = doctor_visit_cost - insurance_covered_amount

    # L3
    cat_visit_cost = 120 # His cat's visit cost $120
    pet_insurance_covered_amount = 60 # his pet insurance covered $60
    paid_for_cat_visit = cat_visit_cost - pet_insurance_covered_amount

    # L4
    total_paid = paid_for_doctor_visit + paid_for_cat_visit

    # FA
    answer = total_paid
    return answer