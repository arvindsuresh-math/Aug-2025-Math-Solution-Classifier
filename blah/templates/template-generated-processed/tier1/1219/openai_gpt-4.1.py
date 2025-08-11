def solve():
    """Index: 1219.
    Returns: the total number of pieces of chicken needed for all the orders.
    """
    # L1
    num_fried_orders = 2 # 2 Fried Chicken Dinner orders
    pieces_per_fried = 8 # family-size Fried Chicken Dinner uses 8 pieces of chicken
    fried_total = num_fried_orders * pieces_per_fried

    # L2
    num_pasta_orders = 6 # 6 Chicken Pasta orders
    pieces_per_pasta = 2 # Chicken Pasta uses 2 pieces of chicken
    pasta_total = num_pasta_orders * pieces_per_pasta

    # L3
    num_bbq_orders = 3 # 3 Barbecue Chicken orders
    pieces_per_bbq = 3 # Barbecue Chicken uses 3 pieces of chicken
    bbq_total = num_bbq_orders * pieces_per_bbq

    # L4
    total_pieces = fried_total + pasta_total + bbq_total

    # FA
    answer = total_pieces
    return answer