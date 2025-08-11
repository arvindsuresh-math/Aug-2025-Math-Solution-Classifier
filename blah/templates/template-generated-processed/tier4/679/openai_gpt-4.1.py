def solve():
    """Index: 679.
    Returns: the total number of pages Bart bought.
    """
    # L1
    total_spent = 10 # Bart buys $10 of notepads
    price_per_notepad = 1.25 # $1.25 each
    num_notepads = total_spent / price_per_notepad

    # L2
    pages_per_notepad = 60 # 60 pages each
    total_pages = num_notepads * pages_per_notepad

    # FA
    answer = total_pages
    return answer