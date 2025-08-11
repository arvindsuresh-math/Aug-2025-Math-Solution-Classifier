def solve():
    """Index: 251.
    Returns: the total money the bakery would make.
    """
    # L1
    pies_made_per_hour = 12 # 12 pies
    pieces_per_pie = 3 # 3 pieces
    total_pie_pieces = pies_made_per_hour * pieces_per_pie

    # L2
    price_per_piece = 4 # $4 for a piece
    total_revenue = total_pie_pieces * price_per_piece

    # L3
    cost_per_pie = 0.5 # Creating one pie costs the bakery $0.5
    total_cost_of_making_pies = pies_made_per_hour * cost_per_pie

    # L4
    net_profit = total_revenue - total_cost_of_making_pies

    # FA
    answer = net_profit
    return answer