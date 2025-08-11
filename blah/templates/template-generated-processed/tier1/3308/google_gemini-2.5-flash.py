def solve():
    """Index: 3308.
    Returns: the total months of work experience Jason has.
    """
    # L1
    bartender_years = 9 # 9 years as a bartender
    months_per_year = 12 # WK
    bartender_months = bartender_years * months_per_year

    # L2
    manager_years = 3 # 3 years
    manager_extra_months = 6 # six months
    manager_months = manager_years * months_per_year + manager_extra_months

    # L3
    total_months = bartender_months + manager_months

    # FA
    answer = total_months
    return answer