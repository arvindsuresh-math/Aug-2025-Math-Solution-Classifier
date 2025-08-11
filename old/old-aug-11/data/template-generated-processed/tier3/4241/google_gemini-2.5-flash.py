from fractions import Fraction

def solve():
    """Index: 4241.
    Returns: the number of marbles each friend received after sharing equally.
    """
    # L1
    wolfgang_marbles = 16 # Wolfgang bought 16 marbles
    ludo_fraction_more = Fraction(1, 4) # 1/4 times more marbles
    ludo_additional_marbles = ludo_fraction_more * wolfgang_marbles

    # L2
    ludo_total_marbles = wolfgang_marbles + ludo_additional_marbles

    # L3
    wolfgang_ludo_combined = ludo_total_marbles + wolfgang_marbles

    # L4
    michael_fraction_of_combined = Fraction(2, 3) # 2/3 times as many marbles
    michael_marbles = michael_fraction_of_combined * wolfgang_ludo_combined

    # L5
    total_marbles_purchased = michael_marbles + wolfgang_ludo_combined

    # L6
    number_of_friends = 3 # Three friends Wolfgang, Ludo, and Michael
    marbles_per_person = total_marbles_purchased / number_of_friends

    # FA
    answer = marbles_per_person
    return answer