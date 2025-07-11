def solve():
    """Index: 1725.
    Returns: the amount Mike paid after insurance.
    """
    # L1
    xray_cost = 250 # The x-ray is $250
    mri_cost_multiplier = 3 # the MRI is triple that cost
    mri_cost = xray_cost * mri_cost_multiplier

    # L2
    total_initial_cost = xray_cost + mri_cost

    # L3
    insurance_coverage_percent = 0.8 # Insurance covers 80%
    insurance_covered_amount = total_initial_cost * insurance_coverage_percent

    # L4
    amount_paid_by_mike = total_initial_cost - insurance_covered_amount

    # FA
    answer = amount_paid_by_mike
    return answer