def solve(
    child_support_rate: float = 0.30, # He's supposed to pay 30% of his income
    initial_years: int = 3, # For 3 years
    initial_salary: int = 30000, # he made $30,000/year
    raise_percentage: float = 0.20, # a 20% raise
    later_years: int = 4, # for the next four years
    amount_paid: int = 1200 # he's only ever paid $1,200
):
    """Index: 6732.
    Returns: the total amount of child support owed.
    """
    #: L1
    initial_earnings = initial_years * initial_salary

    #: L2
    raise_amount = initial_salary * raise_percentage

    #: L3
    new_salary = raise_amount + initial_salary

    #: L4
    later_earnings = later_years * new_salary

    #: L5
    total_earnings = later_earnings + initial_earnings

    #: L6
    total_child_support_due = total_earnings * child_support_rate

    #: L7
    amount_owed = total_child_support_due - amount_paid

    answer = amount_owed # FINAL ANSWER
    return answer