def solve():
    """Index: 594.
    Returns: the total number of shells the pair have altogether.
    """
    # L1
    ed_limpet_shells = 7 # Ed found 7 limpet shells
    ed_oyster_shells = 2 # 2 oyster shells
    ed_conch_shells = 4 # and 4 conch shells
    ed_found_total = ed_limpet_shells + ed_oyster_shells + ed_conch_shells

    # L2
    jacob_more_than_ed = 2 # Jacob found 2 more shells than Ed did
    jacob_found_total = ed_found_total + jacob_more_than_ed

    # L3
    initial_shells = 2 # Ed and Jacob already had 2 shells
    total_shells = initial_shells + ed_found_total + jacob_found_total

    # FA
    answer = total_shells
    return answer