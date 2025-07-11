def solve():
    """Index: 2942.
    Returns: the total amount Gunther financed for the tractor.
    """
    # L1
    months_per_year = 12 # There are 12 months in 1 year
    loan_years = 5 # his loan is for 5 years
    total_months = months_per_year * loan_years

    # L2
    monthly_payment = 150.00 # His monthly payment is $150.00
    total_financed = monthly_payment * total_months

    # FA
    answer = total_financed
    return answer