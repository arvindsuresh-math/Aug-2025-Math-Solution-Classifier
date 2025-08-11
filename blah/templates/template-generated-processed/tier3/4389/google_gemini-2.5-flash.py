def solve():
    """Index: 4389.
    Returns: the difference in monthly payments between the house and the trailer.
    """
    # L1
    loan_years = 20 # over 20 years
    months_per_year = 12 # WK
    total_months = loan_years * months_per_year

    # L2
    house_cost = 480000 # A house costs $480,000
    house_monthly_payment = house_cost / total_months

    # L3
    trailer_cost = 120000 # a trailer costs $120,000
    trailer_monthly_payment = trailer_cost / total_months

    # L4
    payment_difference = house_monthly_payment - trailer_monthly_payment

    # FA
    answer = payment_difference
    return answer