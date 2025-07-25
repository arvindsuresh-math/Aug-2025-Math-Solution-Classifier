def solve():
    """Index: 2650.
    Returns: the total amount of money Jack has in dollars.
    """
    # L1
    euros_jack_has = 36 # 36 euros
    euro_to_dollar_rate = 2 # two dollars
    euros_worth_in_dollars = euros_jack_has * euro_to_dollar_rate

    # L2
    dollars_jack_has = 45 # $45
    total_money_in_dollars = euros_worth_in_dollars + dollars_jack_has

    # FA
    answer = total_money_in_dollars
    return answer