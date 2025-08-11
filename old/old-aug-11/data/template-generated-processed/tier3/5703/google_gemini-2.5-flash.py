def solve():
    """Index: 5703.
    Returns: the number of additional hamburgers Frank needs to sell.
    """
    # L1
    first_purchase_quantity = 4 # 2 people purchased 4
    second_purchase_quantity = 2 # another 2 customers purchased 2 hamburgers
    hamburgers_sold_already = first_purchase_quantity + second_purchase_quantity

    # L2
    price_per_hamburger = 5 # selling each hamburger for $5
    dollars_made_already = price_per_hamburger * hamburgers_sold_already

    # L3
    target_earnings = 50 # wants to sell them to make $50
    dollars_still_needed = target_earnings - dollars_made_already

    # L4
    hamburgers_to_sell = dollars_still_needed / price_per_hamburger

    # FA
    answer = hamburgers_to_sell
    return answer