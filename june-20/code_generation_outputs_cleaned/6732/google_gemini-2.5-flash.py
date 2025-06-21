def solve(
        child_support_rate: float = 0.30, # pay 30% of his income each year
        years_first_period: int = 3, # For 3 years
        income_first_period: int = 30000, # he made $30,000/year
        raise_percentage: float = 0.20, # he got a 20% raise
        years_second_period: int = 4, # for the next four years
        amount_paid: int = 1200 # If he's only ever paid $1,200
    ):
    """Index: 6732.
    Returns: the amount of child support still owed.
    """
    #: L1
    earnings_first_period = years_first_period * income_first_period

    #: L2
    raise_amount = income_first_period * raise_percentage

    #: L3
    income_second_period = income_first_period + raise_amount

    #: L4
    earnings_second_period = years_second_period * income_second_period

    #: L5
    total_earnings = earnings_second_period + earnings_first_period

    #: L6
    total_owed_child_support = total_earnings * child_support_rate

    #: L7
    amount_still_owed = total_owed_child_support - amount_paid

    answer = amount_still_owed # FINAL ANSWER
    return answer