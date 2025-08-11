from fractions import Fraction

def solve():
    """Index: 3021.
    Returns: the number of stamps Jessica needed to mail her letter.
    """
    # L1
    num_papers = 8 # eight pieces of paper
    paper_weight_per_piece = Fraction(1, 5) # weigh 1/5 of an ounce each
    total_paper_weight = num_papers * paper_weight_per_piece

    # L2
    envelope_weight = Fraction(2, 5) # her envelope weighs 2/5 of an ounce
    total_weight_fraction = total_paper_weight + envelope_weight
    total_weight_simplified = int(total_weight_fraction)

    # L3
    stamps_per_ounce = 1 # one stamp per ounce
    stamps_needed = total_weight_simplified * stamps_per_ounce

    # FA
    answer = stamps_needed
    return answer