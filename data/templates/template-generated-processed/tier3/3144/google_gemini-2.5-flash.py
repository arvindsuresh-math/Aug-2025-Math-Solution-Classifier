def solve():
    """Index: 3144.
    Returns: the monthly earnings from Jason's investment.
    """
    # L4
    current_worth = 90 # Jason's investment currently is worth $90
    total_investment_multiplier = 3 # WK
    initial_investment = current_worth / total_investment_multiplier

    # L6
    total_earnings = current_worth - initial_investment

    # L7
    months_invested = 5 # in 5 months
    monthly_returns = total_earnings / months_invested

    # FA
    answer = monthly_returns
    return answer