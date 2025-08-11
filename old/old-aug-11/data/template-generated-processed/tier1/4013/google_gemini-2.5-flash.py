def solve():
    """Index: 4013.
    Returns: the amount of money Kate has left.
    """
    # L1
    saved_march = 27 # saved $27 in March
    saved_april = 13 # saved $13 in April
    saved_may = 28 # saved $28 in May
    total_saved = saved_march + saved_april + saved_may

    # L2
    cost_keyboard = 49 # spent $49 on a keyboard
    cost_mouse = 5 # spent $5 on a mouse
    total_spent = cost_keyboard + cost_mouse

    # L3
    money_left = total_saved - total_spent

    # FA
    answer = money_left
    return answer