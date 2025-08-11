def solve():
    """Index: 6152.
    Returns: the number of apples Kayla picked.
    """
    # L5
    total_apples = 200 # 200 apples total
    # The 4 and 5 are derived from the algebraic simplification of x + (1/4)x = (5/4)x,
    # leading to x = 200 * (4/5). They are numerical values used in the computation.
    # Categorized as question_inputs as they are specific to this problem's numbers and derived from its structure.
    factor_numerator_for_kylie = 4 # from (4/5) in 200(4/5)
    factor_denominator_for_kylie = 5 # from (4/5) in 200(4/5)
    kylie_apples = total_apples * factor_numerator_for_kylie / factor_denominator_for_kylie

    # L6
    kayla_fraction_numerator = 1 # 1/4 of the apples that Kylie picked
    kayla_fraction_denominator = 4 # 1/4 of the apples that Kylie picked
    kayla_apples = kayla_fraction_numerator / kayla_fraction_denominator * kylie_apples

    # FA
    answer = kayla_apples
    return answer