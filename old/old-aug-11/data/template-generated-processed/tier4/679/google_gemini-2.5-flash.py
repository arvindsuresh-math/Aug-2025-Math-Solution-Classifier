def solve():
    """Index: 679.
    Returns: the total number of pages Bart bought.
    """
    # L1
    total_money_spent = 10 # Bart buys $10 of notepads
    cost_per_notepad = 1.25 # for $1.25 each
    num_notepads_bought = total_money_spent / cost_per_notepad

    # L2
    pages_per_notepad = 60 # They have 60 pages each
    total_pages_bought = num_notepads_bought * pages_per_notepad

    # FA
    answer = total_pages_bought
    return answer