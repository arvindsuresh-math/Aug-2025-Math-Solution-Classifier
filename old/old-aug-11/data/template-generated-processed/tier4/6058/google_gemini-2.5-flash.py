def solve():
    """Index: 6058.
    Returns: the number of tubs of ice cream the guests ate.
    """
    # L1
    num_pans = 2 # 2 pans of brownies
    pieces_per_pan = 16 # 16 pieces per pan
    total_brownie_pieces = num_pans * pieces_per_pan

    # L2
    second_pan_percent_eaten = 0.75 # 75% of the 2nd pan
    pieces_eaten_second_pan = pieces_per_pan * second_pan_percent_eaten

    # L3
    total_pieces_eaten = pieces_per_pan + pieces_eaten_second_pan

    # L4
    guests_not_ala_mode = 4 # all but 4 of the guests
    guests_ala_mode = total_pieces_eaten - guests_not_ala_mode

    # L5
    scoops_per_guest = 2 # with 2 scoops of vanilla ice cream
    total_scoops_eaten = guests_ala_mode * scoops_per_guest

    # L6
    scoops_per_tub = 8 # One tub of ice cream provides 8 scoops
    total_tubs_eaten = total_scoops_eaten / scoops_per_tub

    # FA
    answer = total_tubs_eaten
    return answer