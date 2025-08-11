def solve():
    """Index: 6218.
    Returns: the amount of change Blake will get back.
    """
    # L1
    num_lollipops = 4 # 4 lollipops
    cost_per_lollipop = 2 # each lollipop costs $2
    cost_lollipops = cost_per_lollipop * num_lollipops

    # L2
    num_chocolate_packs = 6 # 6 packs of chocolate
    cost_chocolate_packs = cost_lollipops * num_chocolate_packs

    # L3
    total_cost = cost_lollipops + cost_chocolate_packs

    # L4
    bill_denomination = 10 # 6 $10 bills
    num_bills = 6 # 6 $10 bills
    amount_given = bill_denomination * num_bills

    # L5
    change = amount_given - total_cost

    # FA
    answer = change
    return answer