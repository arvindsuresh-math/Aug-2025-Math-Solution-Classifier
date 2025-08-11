def solve():
    """Index: 3839.
    Returns: the number of pieces of gum Quentavious got.
    """
    # L1
    initial_nickels = 5 # 5 nickels
    remaining_nickels = 2 # leaves with 2 nickels
    nickels_spent = initial_nickels - remaining_nickels

    # L2
    pieces_per_nickel = 2 # two pieces per nickel
    total_gum_pieces = nickels_spent * pieces_per_nickel

    # FA
    answer = total_gum_pieces
    return answer