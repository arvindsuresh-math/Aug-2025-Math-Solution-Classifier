def solve():
    """Index: 1037.
    Returns: the total money spent on the computer, counting savings.
    """
    # L1
    new_card_cost = 500 # buys a new one for $500
    old_card_sale_price = 300 # sells the old card for $300
    extra_spent_on_card = new_card_cost - old_card_sale_price

    # L2
    initial_pc_cost = 1200 # buys a gaming PC for $1200
    total_cost = initial_pc_cost + extra_spent_on_card

    # FA
    answer = total_cost
    return answer