def solve():
    """Index: 1127.
    Returns: the number of junk items in the attic.
    """
    # L1
    useful_items_count = 8 # 8 useful items
    useful_items_percent_decimal = 0.2 # 20% of the items are useful
    total_items = useful_items_count / useful_items_percent_decimal

    # L2
    junk_items_percent_decimal = 0.7 # 70% are junk
    junk_items_count = total_items * junk_items_percent_decimal

    # FA
    answer = junk_items_count
    return answer