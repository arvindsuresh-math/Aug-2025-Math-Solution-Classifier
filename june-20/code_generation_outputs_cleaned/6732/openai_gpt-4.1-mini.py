def solve(
    years_first_salary: int = 3,  # For 3 years
    first_salary_per_year: int = 30000,  # he made $30,000/year
    raise_percent: float = 20,  # then he got a 20% raise
    years_second_salary: int = 4,  # for the next four years
    amount_paid: int = 1200  # he's only ever paid $1,200
):
    """Index: 6732.
    Returns: the total amount of child support he still owes.
    """
    #: L1
    earnings_first_period = years_first_salary * first_salary_per_year

    #: L2
    raise_amount = first_salary_per_year * raise_percent * 0.01

    #: L3
    second_salary_per_year = raise_amount + first_salary_per_year

    #: L4
    earnings_second_period = years_second_salary * second_salary_per_year

    #: L5
    total_earnings = earnings_first_period + earnings_second_period

    #: L6
    total_child_support_due = total_earnings * 0.30

    #: L7
    amount_owed = total_child_support_due - amount_paid

    answer = amount_owed  # FINAL ANSWER
    return answer