def solve():
    """Index: 6812.
    Returns: the profit Alice made on the sale of her bracelets.
    """
    # L1
    total_bracelets_made = 52 # Alice made 52 friendship bracelets
    bracelets_given_away = 8 # gave 8 of her bracelets away
    bracelets_remaining = total_bracelets_made - bracelets_given_away

    # L2
    price_per_bracelet = 0.25 # sells all of the remaining bracelets at $0.25 each
    total_sales_revenue = bracelets_remaining * price_per_bracelet

    # L3
    material_cost = 3.00 # cost her $3.00 in materials
    profit = total_sales_revenue - material_cost

    # FA
    answer = profit
    return answer