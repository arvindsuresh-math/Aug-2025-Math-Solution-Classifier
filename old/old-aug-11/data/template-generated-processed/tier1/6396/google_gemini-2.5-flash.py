def solve():
    """Index: 6396.
    Returns: the total amount Jared will earn in a year.
    """
    # L1
    degree_multiplier = 3 # three times the amount paid to a diploma holder
    diploma_pay_per_month = 4000 # $4000 per month
    jared_pay_per_month = diploma_pay_per_month * degree_multiplier

    # L2
    months_per_year = 12 # WK
    jared_pay_per_year = months_per_year * jared_pay_per_month

    # FA
    answer = jared_pay_per_year
    return answer