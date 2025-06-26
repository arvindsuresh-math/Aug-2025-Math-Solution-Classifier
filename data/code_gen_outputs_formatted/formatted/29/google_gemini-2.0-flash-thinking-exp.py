def solve(
    rent_utilities_percent_before: float = 0.40, # spend 40% of her monthly income on rent and utilities
    salary_increase: int = 600, # Her salary was recently increased by $600
    rent_utilities_percent_after: float = 0.25 # now her rent and utilities only amount to 25% of her monthly income
):
    """Index: 29.
    Returns: the previous monthly income.
    """

    #: L6
    lhs_step_6 = 20 * rent_utilities_percent_before
    rhs_multiplier_step_6 = 20 * rent_utilities_percent_after
    rhs_constant_step_6 = rhs_multiplier_step_6 * salary_increase

    #: L7
    lhs_step_7 = lhs_step_6 - rhs_multiplier_step_6

    #: L8
    previous_income = rhs_constant_step_6 / lhs_step_7

    answer = previous_income # FINAL ANSWER
    return answer