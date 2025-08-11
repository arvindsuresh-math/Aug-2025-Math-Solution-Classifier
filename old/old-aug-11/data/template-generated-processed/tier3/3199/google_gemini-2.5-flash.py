def solve():
    """Index: 3199.
    Returns: the total number of sonnets Horatio wrote.
    """
    # L1
    unheard_lines = 70 # 70 romantic lines he wrote that she never heard
    lines_per_sonnet = 14 # Each sonnet is fourteen lines long
    unheard_sonnets = unheard_lines / lines_per_sonnet

    # L2
    read_sonnets = 7 # reads her only seven sonnets
    total_sonnets = read_sonnets + unheard_sonnets

    # FA
    answer = total_sonnets
    return answer