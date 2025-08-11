def solve():
    """Index: 1127.
    Returns: the number of junk items in Marcus's attic.
    """
    # L1
    useful_items = 8 # Marcus's attic has 8 useful items in it
    useful_percent = 0.2 # 20% of the items are useful
    total_items = useful_items / useful_percent

    # L2
    junk_percent = 0.7 # 70% are junk
    junk_items = total_items * junk_percent

    # FA
    answer = junk_items
    return answer