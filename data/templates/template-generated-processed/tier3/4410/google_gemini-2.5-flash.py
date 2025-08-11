def solve():
    """Index: 4410.
    Returns: the total number of bushels of corn Bob will harvest.
    """
    # L1
    num_rows = 5 # 5 rows of corn
    stalks_per_row = 80 # each row has 80 corn stalks
    total_stalks = num_rows * stalks_per_row

    # L2
    stalks_per_bushel = 8 # every 8 corn stalks will produce a bushel of corn
    total_bushels = total_stalks / stalks_per_bushel

    # FA
    answer = total_bushels
    return answer