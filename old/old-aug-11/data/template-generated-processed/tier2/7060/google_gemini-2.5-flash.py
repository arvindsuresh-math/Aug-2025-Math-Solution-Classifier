def solve():
    """Index: 7060.
    Returns: the total amount of money Josh will have in his wallet.
    """
    # L1
    stock_rise_percent_text = 30 # rises 30%
    initial_investment = 2000 # $2000 invested in a business
    percent_factor = 0.01 # WK
    stock_increase_amount = stock_rise_percent_text * percent_factor * initial_investment
    new_stock_value = stock_increase_amount + initial_investment

    # L2
    wallet_money = 300 # $300 in his wallet
    total_money = wallet_money + new_stock_value

    # FA
    answer = total_money
    return answer