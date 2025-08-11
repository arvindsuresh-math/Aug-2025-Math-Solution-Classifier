from fractions import Fraction

def solve():
    """Index: 6791.
    Returns: the total number of stickers Andrew now has.
    """
    # L1
    total_stickers = 1500 # a packet of 1500 stickers
    susan_ratio_part = 1 # in the ratio 1:1:3
    andrew_ratio_part = 1 # in the ratio 1:1:3
    sam_ratio_part = 3 # in the ratio 1:1:3
    sum_of_ratio_parts = susan_ratio_part + andrew_ratio_part + sam_ratio_part
    stickers_per_part = total_stickers / sum_of_ratio_parts

    # L2
    sam_initial_share = sam_ratio_part * stickers_per_part

    # L3
    fraction_given_to_andrew = Fraction(2, 3) # two-thirds of his own share
    stickers_sam_gave_andrew = sam_initial_share * fraction_given_to_andrew

    # L4
    andrew_initial_share = andrew_ratio_part * stickers_per_part

    # L5
    andrew_final_share = andrew_initial_share + stickers_sam_gave_andrew

    # FA
    answer = andrew_final_share
    return answer