def solve():
    """Index: 6693.
    Returns: the total amount John spends on haircuts a year.
    """
    # L1
    max_hair_length = 9 # 9 inches long
    cut_hair_length = 6 # cuts it down to 6 inches
    inches_cut_per_haircut = max_hair_length - cut_hair_length

    # L2
    hair_growth_per_month = 1.5 # grows 1.5 inches every month
    months_per_haircut = inches_cut_per_haircut / hair_growth_per_month

    # L3
    months_per_year = 12 # WK
    haircuts_per_year = months_per_year / months_per_haircut

    # L4
    haircut_cost = 45 # $45
    tip_percent = 0.2 # 20% tip
    tip_amount = haircut_cost * tip_percent

    # L5
    total_cost_per_haircut = haircut_cost + tip_amount

    # L6
    annual_haircut_cost = total_cost_per_haircut * haircuts_per_year

    # FA
    answer = annual_haircut_cost
    return answer