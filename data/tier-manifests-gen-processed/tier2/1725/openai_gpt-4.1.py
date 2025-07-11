def solve():
    """Index: 1725.
    Returns: the amount Mike had to pay after insurance for the x-ray and MRI.
    """
    # L1
    xray_cost = 250 # x-ray is $250
    mri_multiplier = 3 # MRI is triple that cost
    mri_cost = xray_cost * mri_multiplier

    # L2
    total_cost = xray_cost + mri_cost

    # L3
    insurance_coverage_percent = 0.8 # Insurance covers 80%
    insurance_covered_amount = total_cost * insurance_coverage_percent

    # L4
    mike_pays = total_cost - insurance_covered_amount

    # FA
    answer = mike_pays
    return answer