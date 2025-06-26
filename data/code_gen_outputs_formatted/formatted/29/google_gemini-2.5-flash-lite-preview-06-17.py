def solve(
    previous_rent_utility_percentage: float = 0.40, # Mrs. Snyder used to spend 40% of her monthly income on rent and utilities.
    income_increase: int = 600, # Her salary was recently increased by $600
    new_rent_utility_percentage: float = 0.25 # now her rent and utilities only amount to 25% of her monthly income.
):
    """Index: 29.
    Returns: Mrs. Snyder's previous monthly income.
    """

    #: L8
    previous_monthly_income = (new_rent_utility_percentage * income_increase) / (previous_rent_utility_percentage - new_rent_utility_percentage)

    answer = previous_monthly_income # FINAL ANSWER
    return answer