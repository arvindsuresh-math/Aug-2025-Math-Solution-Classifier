def solve():
    """Index: 3937.
    Returns: the total amount Paula and Olive spend.
    """
    # L1
    num_bracelets_paula = 2 # Paula buys two bracelets
    bracelet_price = 4 # bracelets at $4 each
    cost_bracelets_paula = num_bracelets_paula * bracelet_price

    # L2
    keychain_price = 5 # keychains at $5 each
    total_paula_spend = cost_bracelets_paula + keychain_price

    # L3
    coloring_book_price = 3 # coloring books at $3 each
    total_olive_spend = coloring_book_price + bracelet_price

    # L4
    total_spend_both = total_paula_spend + total_olive_spend

    # FA
    answer = total_spend_both
    return answer