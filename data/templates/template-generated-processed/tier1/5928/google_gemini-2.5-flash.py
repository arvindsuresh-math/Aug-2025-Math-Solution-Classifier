def solve():
    """Index: 5928.
    Returns: the total money paid by the three companies for the ads combined.
    """
    # L1
    ad_length = 12 # 12 foot
    ad_width = 5 # 5-foot rectangle
    ad_area = ad_length * ad_width

    # L2
    num_ad_spaces_per_company = 10 # 10 ad spaces
    total_area_per_company = ad_area * num_ad_spaces_per_company

    # L3
    cost_per_sq_ft = 60 # $60
    cost_per_company = cost_per_sq_ft * total_area_per_company

    # L4
    num_companies = 3 # Three companies, A, B, and C
    total_cost_combined = cost_per_company * num_companies

    # FA
    answer = total_cost_combined
    return answer