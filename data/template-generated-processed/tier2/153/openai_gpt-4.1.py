def solve():
    """Index: 153.
    Returns: the total amount Tim paid for both his and his cat's doctor visits.
    """
    # L1
    doctor_visit_cost = 300 # doctor's visits $300
    insurance_coverage_percent = 0.75 # insurance covered 75%
    insurance_coverage_amount = doctor_visit_cost * insurance_coverage_percent

    # L2
    tim_payment = doctor_visit_cost - insurance_coverage_amount

    # L3
    cat_visit_cost = 120 # cat's visit cost $120
    pet_insurance_coverage = 60 # pet insurance covered $60
    cat_payment = cat_visit_cost - pet_insurance_coverage

    # L4
    total_payment = tim_payment + cat_payment

    # FA
    answer = total_payment
    return answer