def solve():
    """Index: 4653.
    Returns: the number of cans Mark brought in.
    """
    # Variables extracted from the question and implied by the algebraic setup
    total_cans_given = 135 # 135 cans total

    # From L2: Jaydon: 5+2x
    jaydon_constant_term = 5 # 5 more
    jaydon_x_coefficient = 2 # twice the amount

    # From L3: Mark: 4(5+2x) = 20+8x
    mark_multiplier = 4 # 4 times as many
    mark_constant = mark_multiplier * jaydon_constant_term
    mark_coefficient = mark_multiplier * jaydon_x_coefficient

    # From L4, L5, L6: Solving x + (5+2x) + (20+8x) = 135
    # Combine x terms: 1x + 2x + 8x = 11x
    combined_x_coefficient = 1 + jaydon_x_coefficient + mark_coefficient
    # Combine constant terms: 5 + 20 = 25
    combined_constant = jaydon_constant_term + mark_constant
    # Equation becomes: 11x + 25 = 135
    # Subtract 25 from both sides: 11x = 135 - 25
    rhs_after_subtraction = total_cans_given - combined_constant

    # L7
    rachel_cans = rhs_after_subtraction / combined_x_coefficient

    # L8
    mark_cans = mark_constant + mark_coefficient * rachel_cans

    # FA
    answer = mark_cans
    return answer