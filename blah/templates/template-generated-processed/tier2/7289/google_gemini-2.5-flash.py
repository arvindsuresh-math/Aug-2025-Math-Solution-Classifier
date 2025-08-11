def solve():
    """Index: 7289.
    Returns: the amount of change Ursula got back.
    """
    # L1
    num_hotdogs = 5 # five hot dogs
    cost_per_hotdog = 1.50 # $1.50 each
    cost_hotdogs = num_hotdogs * cost_per_hotdog

    # L2
    num_salads = 3 # three salads
    cost_per_salad = 2.50 # $2.50 each
    cost_salads = num_salads * cost_per_salad

    # L3
    total_cost_items = cost_hotdogs + cost_salads

    # L4
    num_ten_dollar_bills = 2 # two $10 bills
    bill_denomination = 10 # $10 bills
    total_money_ursula = num_ten_dollar_bills * bill_denomination

    # L5
    change_back = total_money_ursula - total_cost_items

    # FA
    answer = change_back
    return answer