def solve():
    """Index: 388.
    Returns: the total profit John makes in a year.
    """
    # L1
    num_subletters = 3 # 3 people
    rent_per_person_per_month = 400 # $400 per month
    income_from_subletters_per_month = num_subletters * rent_per_person_per_month

    # L2
    months_per_year = 12 # WK
    total_income_per_year = income_from_subletters_per_month * months_per_year

    # L3
    apartment_rent_per_month = 900 # $900 a month
    total_rent_paid_per_year = months_per_year * apartment_rent_per_month

    # L4
    profit_per_year = total_income_per_year - total_rent_paid_per_year

    # FA
    answer = profit_per_year
    return answer