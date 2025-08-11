def solve():
    """Index: 1224.
    Returns: Jim's final portfolio worth after 2 years.
    """
    # L1
    initial_portfolio_amount = 80 # starts with $80 in his investment portfolio
    growth_rate_year1 = 0.15 # grows by 15%
    gain_year1 = initial_portfolio_amount * growth_rate_year1

    # L2
    portfolio_after_year1 = initial_portfolio_amount + gain_year1

    # L3
    added_amount = 28 # adds another $28 to his portfolio
    portfolio_before_year2_growth = portfolio_after_year1 + added_amount

    # L4
    growth_rate_year2_percent = 10 # grows by 10%
    growth_rate_year2_decimal = 0.10 # grows by 10%
    gain_year2 = portfolio_before_year2_growth * growth_rate_year2_decimal

    # L5
    final_portfolio_worth = portfolio_before_year2_growth + gain_year2

    # FA
    answer = final_portfolio_worth
    return answer