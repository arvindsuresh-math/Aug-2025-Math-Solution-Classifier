def solve(
    rent_utilities_percent_before: float = 0.40, # spend 40% of her monthly income on rent and utilities
    salary_increase: int = 600, # Her salary was recently increased by $600
    rent_utilities_percent_after: float = 0.25 # now her rent and utilities only amount to 25% of her monthly income
):
    """Index: 29.
    Returns: the previous monthly income.
    """

    #: L6
    lhs_step_6 = 20 * rent_utilities_percent_before # eval: 8.0 = 20 * 0.4
    rhs_constant_step_6 = rent_utilities_percent_after * salary_increase # eval: 150.0 = 0.25 * 600

    #: L7
    lhs_step_7 = lhs_step_6 - rent_utilities_percent_after # eval: 7.75 = 8.0 - 0.25

    #: L8
    previous_income = rhs_constant_step_6 / lhs_step_7 # eval: 19.35483870967742 = 150.0 / 7.75

    #: FA
    answer = previous_income
    return answer # eval: return 19.35483870967742
