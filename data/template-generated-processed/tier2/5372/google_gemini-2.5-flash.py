def solve():
    """Index: 5372.
    Returns: the total amount of money Annalise spent.
    """
    # L1
    packs_per_box = 20 # each box has 20 packs of tissues
    num_boxes = 10 # buy 10 boxes
    total_packs = packs_per_box * num_boxes

    # L2
    tissues_per_pack = 100 # each pack contain 100 tissues
    total_tissues = tissues_per_pack * total_packs

    # L3
    cost_per_tissue = 0.05 # sold at five cents each
    total_cost = total_tissues * cost_per_tissue

    # FA
    answer = total_cost
    return answer