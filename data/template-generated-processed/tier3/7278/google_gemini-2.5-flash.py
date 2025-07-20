def solve():
    """Index: 7278.
    Returns: the total amount Mrs. Garcia pays in a year for her insurance.
    """
    # L1
    months_per_year = 12 # WK
    months_per_quarter = 3 # three months in a quarter
    quarters_per_year = months_per_year / months_per_quarter

    # L2
    quarterly_payment = 378 # $378
    annual_payment = quarterly_payment * quarters_per_year

    # FA
    answer = annual_payment
    return answer