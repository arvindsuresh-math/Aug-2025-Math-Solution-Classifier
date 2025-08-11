def solve():
    """Index: 385.
    Returns: the total pounds of strawberry picked.
    """
    # L1
    entry_charge_per_person = 4 # Miguel charges each interested picker $4
    number_of_pickers = 3 # Sally, Jenny and Moses
    total_entry_charge = entry_charge_per_person * number_of_pickers

    # L2
    final_paid_cost = 128 # They paid $128 for their harvest
    cost_before_discount = final_paid_cost + total_entry_charge

    # L3
    price_per_pound = 20 # the standard price of a pound of strawberries is $20
    pounds_picked = cost_before_discount / price_per_pound

    # FA
    answer = pounds_picked
    return answer