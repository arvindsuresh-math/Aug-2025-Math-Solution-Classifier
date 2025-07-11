def solve():
    """Index: 1934.
    Returns: the total amount Jeff paid for the apartment over 5 years.
    """
    # L1
    monthly_rent_initial = 300 # $300 each month
    months_per_year = 12 # WK
    yearly_rent_initial = monthly_rent_initial * months_per_year

    # L2
    years_initial = 3 # first 3 years
    total_initial = yearly_rent_initial * years_initial

    # L3
    monthly_rent_final = 350 # $350 each month
    yearly_rent_final = monthly_rent_final * months_per_year

    # L4
    years_final = 2 # final 2 years
    total_final = yearly_rent_final * years_final

    # L5
    total_paid = total_initial + total_final

    # FA
    answer = total_paid
    return answer