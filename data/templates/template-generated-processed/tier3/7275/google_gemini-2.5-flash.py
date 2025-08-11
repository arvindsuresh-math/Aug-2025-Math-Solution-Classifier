def solve():
    """Index: 7275.
    Returns: the number of Slurpees John bought.
    """
    # L1
    total_given_money = 20 # gives them $20
    change_received = 8 # got $8 in change
    money_spent_on_slurpees = total_given_money - change_received

    # L2
    cost_per_slurpee = 2 # Slurpees cost $2 each
    number_of_slurpees = money_spent_on_slurpees / cost_per_slurpee

    # FA
    answer = number_of_slurpees
    return answer