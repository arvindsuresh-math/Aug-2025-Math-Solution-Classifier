def solve(
    rent_utilities_percent_before: float = 0.40, # spend 40% of her monthly income on rent and utilities
    salary_increase: int = 600, # Her salary was recently increased by $600
    rent_utilities_percent_after: float = 0.25 # now her rent and utilities only amount to 25% of her monthly income
):
    """Index: 29.
    Returns: the previous monthly income.
    """
    # Let previous_income be p
    # The cost of rent and utilities is constant.
    # Before: rent_utilities_percent_before * previous_income
    # After: rent_utilities_percent_after * (previous_income + salary_increase)
    # So, rent_utilities_percent_before * previous_income = rent_utilities_percent_after * (previous_income + salary_increase)
    # 0.4 * p = 0.25 * (p + 600)
    # 0.4p = 0.25p + 0.25 * 600
    # 0.4p = 0.25p + 150
    # 0.4p - 0.25p = 150
    # 0.15p = 150
    # p = 150 / 0.15

    # The solution uses algebraic steps to solve the equation 2p/5 = (p+600)/4
    # This is equivalent to 0.4p = 0.25(p+600)

    #: L6
    # Multiply both sides by 20 to clear fractions (or decimals)
    # 20 * 0.4 * previous_income = 20 * 0.25 * (previous_income + salary_increase)
    lhs_step_6 = 20 * rent_utilities_percent_before
    rhs_multiplier_step_6 = 20 * rent_utilities_percent_after
    # This gives 8 * previous_income = 5 * (previous_income + salary_increase)
    # 8 * previous_income = 5 * previous_income + 5 * salary_increase
    rhs_constant_step_6 = rhs_multiplier_step_6 * salary_increase # 5 * 600 = 3000

    #: L7
    # Subtract 5 * previous_income from both sides
    # 8 * previous_income - 5 * previous_income = 5 * salary_increase
    lhs_step_7 = lhs_step_6 - rhs_multiplier_step_6 # 8 - 5 = 3
    # This gives 3 * previous_income = 3000

    #: L8
    # Divide both sides by 3
    previous_income = rhs_constant_step_6 / lhs_step_7 # 3000 / 3 = 1000

    answer = previous_income # FINAL ANSWER
    return answer