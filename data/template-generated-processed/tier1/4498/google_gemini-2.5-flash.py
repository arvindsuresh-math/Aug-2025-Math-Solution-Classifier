def solve():
    """Index: 4498.
    Returns: the length of the boards before the final cut.
    """
    # L1
    initial_length = 143 # cut the wood to 143 cm
    first_cut_amount = 25 # cut 25 cm off the board
    length_after_first_cut = initial_length - first_cut_amount

    # L2
    cut_off_to_match = 7 # cut off 7 cm from each
    length_before_final_cut = length_after_first_cut + cut_off_to_match

    # FA
    answer = length_before_final_cut
    return answer