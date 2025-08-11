def solve():
    """Index: 2110.
    Returns: Julia's change after buying items.
    """
    # L1
    snickers_cost_per_piece = 1.5 # each piece of Snickers costs $1.5
    num_snickers_pieces = 2 # 2 pieces of Snickers
    cost_snickers = snickers_cost_per_piece * num_snickers_pieces

    # L2
    snickers_per_mms_pack = 2 # a pack of M&M's has the same cost as 2 Snickers
    cost_one_mms_pack = snickers_cost_per_piece * snickers_per_mms_pack
    num_mms_packs = 3 # 3 packs of M&M's
    cost_mms = cost_one_mms_pack * num_mms_packs

    # L3
    total_cost_items = cost_snickers + cost_mms

    # L4
    bill_denomination = 10 # 2 $10 bills
    num_bills = 2 # 2 $10 bills
    amount_given = bill_denomination * num_bills

    # L5
    change = amount_given - total_cost_items

    # FA
    answer = change
    return answer