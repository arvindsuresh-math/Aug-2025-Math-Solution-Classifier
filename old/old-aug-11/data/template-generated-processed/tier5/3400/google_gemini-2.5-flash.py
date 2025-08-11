def solve():
    """Index: 3400.
    Returns: the amount Rodney can lift.
    """
    # The solution involves algebraic steps (L1-L6) to set up and simplify an equation.
    # The numerical values for coefficients and constants used in L7 and L8 are derived
    # from the problem statement's relationships.

    # Define initial numerical values from the question
    combined_total_weight = 239 # combined weight of 239 pounds

    # Define derived coefficients and constants from the algebraic setup (L1-L6)
    # These are treated as WK_inputs in logical_steps as they are not direct question inputs
    # and are not outputs of prior formalized computational steps.
    total_x_coefficient = 13 # WK
    total_constant_term = 21 # WK
    rodney_simplified_coefficient = 8 # WK
    rodney_simplified_constant = 14 # WK

    # L7
    # From the equation 13x - 21 = 239, we get 13x = 239 + 21
    rhs_after_constant_move = combined_total_weight + total_constant_term
    ron_lift = rhs_after_constant_move / total_x_coefficient

    # L8
    # Rodney's lift is 8x - 14
    rodney_lift = rodney_simplified_coefficient * ron_lift - rodney_simplified_constant

    # FA
    answer = rodney_lift
    return answer