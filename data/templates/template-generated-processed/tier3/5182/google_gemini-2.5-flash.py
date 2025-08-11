def solve():
    """Index: 5182.
    Returns: the cost of each wand Kate paid.
    """
    # L1
    wands_purchased = 3 # buys 3 magic wands
    wands_kept = 1 # one for herself
    wands_sold = wands_purchased - wands_kept

    # L2
    total_collected = 130 # collected $130 after the sale
    charge_per_wand = total_collected / wands_sold

    # L3
    markup_per_wand = 5 # for $5 more than she paid
    cost_per_wand = charge_per_wand - markup_per_wand

    # FA
    answer = cost_per_wand
    return answer