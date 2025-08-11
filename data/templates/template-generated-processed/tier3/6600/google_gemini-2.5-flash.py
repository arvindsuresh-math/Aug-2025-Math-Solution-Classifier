def solve():
    """Index: 6600.
    Returns: the total number of pies Chef Michel sold.
    """
    # L1
    shepherds_pie_customers = 52 # 52 customers ordered slices of shepherd's pie
    shepherds_pie_pieces_per_pie = 4 # shepherd's pie cut into 4 pieces
    shepherds_pies_sold = shepherds_pie_customers / shepherds_pie_pieces_per_pie

    # L2
    chicken_pot_pie_customers = 80 # 80 customers ordered slices of chicken pot pie
    chicken_pot_pie_pieces_per_pie = 5 # chicken pot pie cut into 5 pieces
    chicken_pot_pies_sold = chicken_pot_pie_customers / chicken_pot_pie_pieces_per_pie

    # L3
    total_pies_sold = shepherds_pies_sold + chicken_pot_pies_sold

    # FA
    answer = total_pies_sold
    return answer