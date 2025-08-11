def solve():
    """Index: 2942.
    Returns: the total amount the tractor was financed for.
    """
    # L1
    months_per_year = 12 # WK
    loan_duration_years = 5 # for 5 years
    total_months = months_per_year * loan_duration_years

    # L2
    monthly_payment = 150.00 # $150.00 a month
    total_financed_amount = monthly_payment * total_months

    # FA
    answer = total_financed_amount
    return answer