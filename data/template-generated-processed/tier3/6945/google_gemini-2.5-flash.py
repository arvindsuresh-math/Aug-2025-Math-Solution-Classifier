def solve():
    """Index: 6945.
    Returns: the total cost in dollars Josh paid.
    """
    # L1
    pieces_per_pack = 20 # Each pack has 20 string cheeses
    cost_per_piece_cents = 10 # Each piece of string cheese cost 10 cents
    cost_per_pack_cents = pieces_per_pack * cost_per_piece_cents

    # L2
    cents_per_dollar = 100 # WK
    cost_per_pack_dollars = cost_per_pack_cents / cents_per_dollar

    # L3
    num_packs = 3 # Josh buys 3 packs of string cheese
    total_cost_dollars = cost_per_pack_dollars * num_packs

    # FA
    answer = total_cost_dollars
    return answer