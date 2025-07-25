def solve():
    """Index: 7413.
    Returns: the profit Company A gets.
    """
    # L2
    company_b_profit_percent_num = 40 # company B receives 40% of the profits
    company_b_profit_amount = 60000 # company B gets a total of $60000 in profit
    percent_factor = 0.01 # WK
    company_b_profit_percent_decimal = company_b_profit_percent_num * percent_factor

    # L3
    total_profit = company_b_profit_amount / company_b_profit_percent_decimal

    # L4
    company_a_profit_percent_num = 60 # Company A receives 60% of the combined profits
    company_a_profit_percent_decimal = company_a_profit_percent_num * percent_factor
    company_a_profit_amount = company_a_profit_percent_decimal * total_profit

    # FA
    answer = company_a_profit_amount
    return answer