def solve():
    """Index: 1770.
    Returns: the length of each body section of the essay.
    """
    # L1
    introduction_length = 450 # The introduction will be 450 words
    triple_factor = 3 # triple the length of the introduction
    conclusion_length = introduction_length * triple_factor

    # L2
    total_essay_length = 5000 # If her essay has to be 5000 words total
    combined_body_sections_length = total_essay_length - conclusion_length - introduction_length

    # L3
    num_body_sections = 4 # each of the four body sections
    length_per_section = combined_body_sections_length / num_body_sections

    # FA
    answer = length_per_section
    return answer