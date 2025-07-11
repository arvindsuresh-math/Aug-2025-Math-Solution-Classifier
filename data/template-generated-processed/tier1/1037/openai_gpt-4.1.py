def solve():
    """Index: 1037.
    Returns: the total amount John spent on his computer, accounting for selling the old video card.
    """
    # L1
    new_card_cost = 500 # buys a new one for $500
    old_card_sale = 300 # sells the old card for $300
    extra_spent_on_card = new_card_cost - old_card_sale

    # L2
    pc_base_cost = 1200 # buys a gaming PC for $1200
    total_cost = pc_base_cost + extra_spent_on_card

    # FA
    answer = total_cost
    return answer