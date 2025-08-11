def solve():
    """Index: 6679.
    Returns: the amount of money Oliver has left.
    """
    # L1
    initial_money = 9 # Oliver had $9
    saved_from_allowance = 5 # saved $5 from his allowance
    money_after_saving = initial_money + saved_from_allowance

    # L2
    cost_frisbee = 4 # spent $4 on a frisbee
    cost_puzzle = 3 # spent $3 on a puzzle
    total_spent = cost_frisbee + cost_puzzle

    # L3
    money_after_spending = money_after_saving - total_spent

    # L4
    birthday_money = 8 # friend gives him another $8
    final_money = money_after_spending + birthday_money

    # FA
    answer = final_money
    return answer