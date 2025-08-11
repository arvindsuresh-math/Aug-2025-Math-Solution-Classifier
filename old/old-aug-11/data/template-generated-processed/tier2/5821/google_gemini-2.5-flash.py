def solve():
    """Index: 5821.
    Returns: James's out-of-pocket cost for the doctor visit.
    """
    # L1
    visit_charge = 300 # primary care doctor charges $300 for the visit
    insurance_coverage_percent = 0.8 # insurance covers 80%
    insurance_covered_amount = visit_charge * insurance_coverage_percent

    # L2
    out_of_pocket_cost = visit_charge - insurance_covered_amount

    # FA
    answer = out_of_pocket_cost
    return answer