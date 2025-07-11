from fractions import Fraction

def solve():
    """Index: 2205.
    Returns: the total number of apples Frank and Susan have left.
    """
    # L1
    frank_apples = 36 # Frank picked 36 apples
    susan_multiplier = 3 # Susan picked 3 times as many apples as Frank
    susan_initial_apples = susan_multiplier * frank_apples

    # L2
    susan_given_out_fraction = Fraction(1, 2) # Susan gave out half of her apples
    susan_apples_given_out = susan_initial_apples * susan_given_out_fraction

    # L3
    susan_remaining_apples = susan_initial_apples - susan_apples_given_out

    # L4
    frank_sold_fraction = Fraction(1, 3) # Frank sold a third of his
    frank_apples_sold = frank_apples * frank_sold_fraction

    # L5
    frank_remaining_apples = frank_apples - frank_apples_sold

    # L6
    total_remaining_apples = susan_remaining_apples + frank_remaining_apples

    # FA
    answer = total_remaining_apples
    return answer