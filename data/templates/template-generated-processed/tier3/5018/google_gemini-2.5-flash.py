def solve():
    """Index: 5018.
    Returns: the price of a pack of cheese cookies.
    """
    # L1
    boxes_per_carton = 12 # 1 carton contains 12 boxes
    dozen_cartons = 12 # a dozen cartons
    total_boxes_in_dozen_cartons = boxes_per_carton * dozen_cartons

    # L2
    packs_per_box = 10 # each box has 10 packs of cheese cookies
    total_packs_in_dozen_cartons = total_boxes_in_dozen_cartons * packs_per_box

    # L3
    cost_of_dozen_cartons = 1440 # a dozen cartons cost $1440
    price_per_pack = cost_of_dozen_cartons / total_packs_in_dozen_cartons

    # FA
    answer = price_per_pack
    return answer