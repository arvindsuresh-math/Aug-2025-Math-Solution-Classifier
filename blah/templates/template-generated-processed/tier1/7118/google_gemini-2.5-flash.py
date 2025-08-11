def solve():
    """Index: 7118.
    Returns: the total number of white roses needed.
    """
    # L1
    num_table_decorations = 7 # 7 table decorations
    roses_per_table_decoration = 12 # 12 white roses in each table decoration
    roses_for_table_decorations = num_table_decorations * roses_per_table_decoration

    # L2
    num_bouquets = 5 # 5 bouquets
    roses_per_bouquet = 5 # 5 white roses in each bouquet
    roses_for_bouquets = num_bouquets * roses_per_bouquet

    # L3
    total_white_roses = roses_for_table_decorations + roses_for_bouquets

    # FA
    answer = total_white_roses
    return answer