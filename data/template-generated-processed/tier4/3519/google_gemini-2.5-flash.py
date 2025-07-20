def solve():
    """Index: 3519.
    Returns: the money required per person for ice cream bars.
    """
    # L1
    num_friends = 6 # 6 friends
    bars_per_friend = 2 # each eat 2 bars
    total_bars_needed = num_friends * bars_per_friend

    # L2
    bars_per_box = 3 # contains three bars
    total_boxes_needed = total_bars_needed / bars_per_box

    # L3
    cost_per_box = 7.50 # A box of ice cream bars costs $7.50
    total_cost = total_boxes_needed * cost_per_box

    # L4
    cost_per_person = total_cost / num_friends

    # FA
    answer = cost_per_person
    return answer