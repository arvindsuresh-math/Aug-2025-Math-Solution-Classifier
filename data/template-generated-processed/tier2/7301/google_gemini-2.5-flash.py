def solve():
    """Index: 7301.
    Returns: the total money contributed to her 401k after 1 year.
    """
    # L1
    contribution_per_paycheck = 100.00 # puts $100.00 from every paycheck
    paychecks_per_year = 26 # 26 paychecks per year
    annual_personal_contribution = contribution_per_paycheck * paychecks_per_year

    # L2
    match_rate_decimal = 0.06 # by 6%
    company_contribution_per_paycheck = contribution_per_paycheck * match_rate_decimal

    # L3
    annual_company_contribution = company_contribution_per_paycheck * paychecks_per_year

    # L4
    total_annual_contribution = annual_personal_contribution + annual_company_contribution

    # FA
    answer = total_annual_contribution
    return answer