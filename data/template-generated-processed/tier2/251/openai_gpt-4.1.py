def solve():
    """Index: 251.
    Returns: the total money the bakery would make after costs.
    """
    # L1
    pies_made = 12 # bakery can make 12 pies
    pieces_per_pie = 3 # each pie is having 3 pieces
    total_pieces = pies_made * pieces_per_pie

    # L2
    price_per_piece = 4 # one pie costs $4 for a piece
    total_revenue = total_pieces * price_per_piece

    # L3
    cost_per_pie = 0.5 # creating one pie costs the bakery $0.5
    total_cost = pies_made * cost_per_pie

    # L4
    net_profit = total_revenue - total_cost

    # FA
    answer = net_profit
    return answer