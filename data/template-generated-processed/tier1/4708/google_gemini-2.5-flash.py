def solve():
    """Index: 4708.
    Returns: the amount of money left in Mirasol's account.
    """
    # L1
    tumbler_cost = 30 # spent $30 on a tumbler
    coffee_beans_cost = 10 # spent $10 on coffee beans
    total_spent = tumbler_cost + coffee_beans_cost

    # L2
    initial_amount = 50 # had $50 in her account
    amount_left = initial_amount - total_spent

    # FA
    answer = amount_left
    return answer