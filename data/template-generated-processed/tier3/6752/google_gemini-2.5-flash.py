def solve():
    """Index: 6752.
    Returns: the number of apples in each slice of pie.
    """
    # L1
    num_dozens = 4 # four dozen Granny Smith apples
    items_per_dozen = 12 # WK
    total_apples = num_dozens * items_per_dozen

    # L2
    num_pies = 4 # four apple pies
    pieces_per_pie = 6 # 6 large pieces
    total_pieces = num_pies * pieces_per_pie

    # L3
    apples_per_slice = total_apples / total_pieces

    # FA
    answer = apples_per_slice
    return answer