def solve():
    """Index: 5668.
    Returns: the number of days the printer paper will last the office.
    """
    # L1
    num_packs = 2 # two packs of printer paper
    sheets_per_pack = 240 # Each pack has 240 sheets of paper
    total_sheets = num_packs * sheets_per_pack

    # L2
    pages_per_day = 80 # prints 80 one-page documents per day
    days_last = total_sheets / pages_per_day

    # FA
    answer = days_last
    return answer