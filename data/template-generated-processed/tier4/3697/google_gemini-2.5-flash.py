def solve():
    """Index: 3697.
    Returns: the total amount Opal put into her savings.
    """
    # L1
    initial_winnings = 100.00 # Opal won $100.00
    savings_divisor_first_bet = 2 # half of her winnings
    savings_first_bet = initial_winnings / savings_divisor_first_bet

    # L2
    amount_to_bet_second_time = initial_winnings - savings_first_bet

    # L3
    profit_rate_second_bet = 0.60 # made a 60% profit
    profit_second_bet = amount_to_bet_second_time * profit_rate_second_bet

    # L4
    total_earnings_second_bet = profit_second_bet + amount_to_bet_second_time

    # L5
    savings_divisor_second_bet = 2 # half of her earnings
    savings_second_bet = total_earnings_second_bet / savings_divisor_second_bet

    # L6
    total_savings = savings_first_bet + savings_second_bet

    # FA
    answer = total_savings
    return answer