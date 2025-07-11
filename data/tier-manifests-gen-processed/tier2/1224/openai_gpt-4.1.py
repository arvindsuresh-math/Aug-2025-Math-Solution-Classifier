def solve():
    """Index: 1224.
    Returns: Jim's final portfolio value after 2 years.
    """
    # L1
    initial_portfolio = 80 # Jim starts with $80
    first_year_growth_rate = 0.15 # grows by 15%
    first_year_gain = initial_portfolio * first_year_growth_rate

    # L2
    after_first_year = initial_portfolio + first_year_gain

    # L3
    additional_investment = 28 # adds another $28
    portfolio_after_addition = after_first_year + additional_investment

    # L4
    second_year_growth_rate = 0.10 # grows by 10%
    second_year_gain = portfolio_after_addition * second_year_growth_rate

    # L5
    final_portfolio = portfolio_after_addition + second_year_gain

    # FA
    answer = final_portfolio
    return answer