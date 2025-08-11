def solve():
    """Index: 5991.
    Returns: the final balance as a percentage of the starting balance.
    """
    # L1
    initial_balance = 125 # Megan’s grandma gave her $125
    increase_percent_decimal = 0.25 # increased by 25%
    increase_percent_num = 25 # increased by 25%
    increase_amount = increase_percent_decimal * initial_balance
    balance_after_increase = initial_balance + increase_amount

    # L2
    decrease_percent_decimal = 0.20 # decreased by 20%
    decrease_percent_num = 20 # decreased by 20%
    decrease_amount = decrease_percent_decimal * balance_after_increase
    final_balance = balance_after_increase - decrease_amount

    # L3
    percentage_of_starting_balance = (final_balance / initial_balance) * 100

    # FA
    answer = percentage_of_starting_balance
    return answer