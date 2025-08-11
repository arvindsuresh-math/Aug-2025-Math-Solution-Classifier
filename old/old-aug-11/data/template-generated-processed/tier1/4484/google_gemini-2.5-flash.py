def solve():
    """Index: 4484.
    Returns: the total amount Diego saves over a year.
    """
    # L1
    paycheck = 5000 # $5,000 paycheck
    expenses = 4600 # $4,600 per month
    monthly_savings = paycheck - expenses

    # L2
    months_per_year = 12 # WK
    annual_savings = months_per_year * monthly_savings

    # FA
    answer = annual_savings
    return answer