def solve():
    """Index: 3855.
    Returns: the total money Meadow makes from selling all her diapers.
    """
    # L1
    num_boxes = 30 # orders 30 boxes of diapers
    packs_per_box = 40 # containing 40 packs weekly
    total_packs = num_boxes * packs_per_box

    # L2
    diapers_per_pack = 160 # each pack having 160 diapers
    total_diapers = total_packs * diapers_per_pack

    # L3
    price_per_diaper = 5 # sells each diaper for $5
    total_money = total_diapers * price_per_diaper

    # FA
    answer = total_money
    return answer