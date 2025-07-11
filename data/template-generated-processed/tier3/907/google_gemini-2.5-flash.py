def solve():
    """Index: 907.
    Returns: the number of pallets of paper cups received by the store.
    """
    # L1
    total_pallets = 20 # 20 pallets of paper products
    half_divisor = 2 # Half the pallets
    paper_towels_pallets = total_pallets / half_divisor

    # L2
    quarter_divisor = 4 # a quarter were tissues
    tissues_pallets = total_pallets / quarter_divisor

    # L3
    fifth_divisor = 5 # a fifth were paper plates
    paper_plates_pallets = total_pallets / fifth_divisor

    # L4
    paper_cups_pallets = total_pallets - paper_towels_pallets - tissues_pallets - paper_plates_pallets

    # FA
    answer = paper_cups_pallets
    return answer