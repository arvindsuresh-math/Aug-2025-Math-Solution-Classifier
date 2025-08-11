def solve():
    """Index: 926.
    Returns: the total amount Bailey will spend on towel sets after the discount.
    """
    # L1
    num_guest_sets = 2 # 2 new sets of towels for the guest bathroom
    guest_set_price = 40.00 # set of towels for the guest bathroom are $40.00 each
    guest_total = num_guest_sets * guest_set_price

    # L2
    num_master_sets = 4 # 4 new sets for her master bathroom
    master_set_price = 50.00 # master bathroom set is $50.00 each
    master_total = num_master_sets * master_set_price

    # L3
    towels_total = guest_total + master_total

    # L4
    discount_percent_decimal = 0.20 # 20% off
    discount_amount = towels_total * discount_percent_decimal

    # L5
    final_total = towels_total - discount_amount

    # FA
    answer = final_total
    return answer