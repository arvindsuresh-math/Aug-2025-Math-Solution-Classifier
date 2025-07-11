from fractions import Fraction

def solve():
    """Index: 2389.
    Returns: the expected number of times a card that's both red and has a number divisible by 3 is picked.
    """
    # L1
    red_card_probability = Fraction(1, 2) # WK
    divisible_by_3_probability = Fraction(1, 3) # odds of drawing a card divisible by 3 are 1/3

    # L2
    combined_probability = divisible_by_3_probability * red_card_probability

    # L3
    num_draws = 36 # Mark picks a card at random and then replaces it 36 times
    expected_picks = combined_probability * num_draws

    # FA
    answer = expected_picks
    return answer