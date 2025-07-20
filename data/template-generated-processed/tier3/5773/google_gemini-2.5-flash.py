from fractions import Fraction

def solve():
    """Index: 5773.
    Returns: the number of gnomes remaining in Ravenswood forest.
    """
    # L1
    gnomes_westerville = 20 # 20 gnomes in Westerville woods
    ravenswood_multiplier = 4 # four times as many gnomes
    gnomes_ravenswood = ravenswood_multiplier * gnomes_westerville

    # L2
    percentage_taken = Fraction(40, 100) # 40% of the gnomes are taken
    gnomes_taken = percentage_taken * gnomes_ravenswood

    # L3
    remaining_gnomes = gnomes_ravenswood - gnomes_taken

    # FA
    answer = remaining_gnomes
    return answer