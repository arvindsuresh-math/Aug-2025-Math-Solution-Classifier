def solve():
    """Index: 594.
    Returns: the total number of shells Ed and Jacob have altogether.
    """
    # L1
    ed_limpet = 7 # Ed found 7 limpet shells
    ed_oyster = 2 # Ed found 2 oyster shells
    ed_conch = 4 # Ed found 4 conch shells
    ed_found = ed_limpet + ed_oyster + ed_conch

    # L2
    jacob_more_than_ed = 2 # Jacob found 2 more shells than Ed did
    jacob_found = ed_found + jacob_more_than_ed

    # L3
    already_had = 2 # already had 2 shells
    total_shells = already_had + ed_found + jacob_found

    # FA
    answer = total_shells
    return answer