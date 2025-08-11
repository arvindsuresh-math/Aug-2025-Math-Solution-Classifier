def solve():
    """Index: 6551.
    Returns: the amount of money Troy still needs to buy the new computer.
    """
    # L1
    initial_savings = 50 # saved $50
    old_computer_sale = 20 # sell his old computer for $20
    total_money_saved = initial_savings + old_computer_sale

    # L2
    computer_cost = 80 # worth $80
    money_needed = computer_cost - total_money_saved

    # FA
    answer = money_needed
    return answer