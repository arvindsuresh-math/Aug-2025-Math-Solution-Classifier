def solve(
        initial_rent_utilities_percentage: float = 0.40, # 40% of her monthly income on rent and utilities
        salary_increase: int = 600, # Her salary was recently increased by $600
        new_rent_utilities_percentage: float = 0.25 # now her rent and utilities only amount to 25% of her monthly income
    ):
    """Index: 29.
    Returns: her previous monthly income.
    """

    #: L6
    right_side_constant_term = 5 * salary_increase # eval: 3000 = 5 * 600

    #: L7
    coefficient_of_p = 3 # eval: 3 = 3

    #: L8
    previous_monthly_income = right_side_constant_term / coefficient_of_p # eval: 1000.0 = 3000 / 3

    #: FA
    answer = previous_monthly_income # eval: 1000.0 = 1000.0
    return answer # eval: return 1000.0
