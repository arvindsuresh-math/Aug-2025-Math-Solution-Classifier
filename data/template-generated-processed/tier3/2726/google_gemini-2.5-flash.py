def solve():
    """Index: 2726.
    Returns: the value of the middle letter before the word score was tripled.
    """
    # L1
    total_score_tripled = 30 # thirty points
    triple_factor = 3 # triple word score
    score_before_tripling = total_score_tripled / triple_factor

    # L2
    first_letter_value = 1 # first and third letters were each valued at one point apiece
    third_letter_value = 1 # first and third letters were each valued at one point apiece
    middle_letter_value = score_before_tripling - first_letter_value - third_letter_value

    # FA
    answer = middle_letter_value
    return answer