def solve():
    """Index: 3213.
    Returns: the total money Teal makes from her sales.
    """
    # L1
    pumpkin_pie_pieces_per_pie = 8 # The pumpkin pie is cut into 8 pieces.
    num_pumpkin_pies_sold = 4 # Teal sells 4 pumpkin pies
    total_pumpkin_slices = pumpkin_pie_pieces_per_pie * num_pumpkin_pies_sold

    # L2
    custard_pie_pieces_per_pie = 6 # The custard pie is cut into 6 pieces.
    num_custard_pies_sold = 5 # and 5 custard pies
    total_custard_slices = custard_pie_pieces_per_pie * num_custard_pies_sold

    # L3
    price_per_pumpkin_slice = 5 # Pumpkin pie is $5 a slice.
    total_pumpkin_sales = total_pumpkin_slices * price_per_pumpkin_slice

    # L4
    price_per_custard_slice = 6 # Custard pie is $6 a slice.
    total_custard_sales = total_custard_slices * price_per_custard_slice

    # L5
    total_money_made = total_pumpkin_sales + total_custard_sales

    # FA
    answer = total_money_made
    return answer