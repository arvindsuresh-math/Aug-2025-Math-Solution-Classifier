def solve():
    """Index: 3559.
    Returns: the cost of each slice of bread in cents.
    """
    # L1
    num_20_dollar_bills = 2 # 2 $20 bills
    value_of_20_dollar_bill = 20 # 2 $20 bills
    total_money_given = num_20_dollar_bills * value_of_20_dollar_bill

    # L2
    change_received = 16 # $16 change
    total_cost = total_money_given - change_received

    # L3
    num_loaves = 3 # 3 loaves of bread
    cost_per_loaf = total_cost / num_loaves

    # L4
    cents_per_dollar = 100 # WK
    cost_per_loaf_in_cents = cost_per_loaf * cents_per_dollar

    # L5
    slices_per_loaf = 20 # Each loaf of bread has 20 slices
    cost_per_slice_in_cents = cost_per_loaf_in_cents / slices_per_loaf

    # FA
    answer = cost_per_slice_in_cents
    return answer