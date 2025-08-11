def solve():
    """Index: 6664.
    Returns: the cost of one box of tissues.
    """
    # L1
    num_toilet_paper_rolls = 10 # 10 rolls of toilet paper
    cost_toilet_paper_per_roll = 1.50 # One roll of toilet paper costs $1.50
    total_cost_toilet_paper = num_toilet_paper_rolls * cost_toilet_paper_per_roll

    # L2
    num_paper_towel_rolls = 7 # 7 rolls of paper towels
    cost_paper_towel_per_roll = 2 # One roll of paper towels costs $2
    total_cost_paper_towels = num_paper_towel_rolls * cost_paper_towel_per_roll

    # L3
    total_cost_all_items = 35 # total cost of all the items is $35
    total_cost_tissues = total_cost_all_items - total_cost_toilet_paper - total_cost_paper_towels

    # L4
    num_tissue_boxes = 3 # 3 boxes of tissues
    cost_one_box_tissues = total_cost_tissues / num_tissue_boxes

    # FA
    answer = cost_one_box_tissues
    return answer