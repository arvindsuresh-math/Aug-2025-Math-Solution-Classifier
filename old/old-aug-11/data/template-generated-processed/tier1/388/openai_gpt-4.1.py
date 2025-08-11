def solve():
    """Index: 388.
    Returns: the profit John makes in a year from subletting his apartment.
    """
    # L1
    num_subletters = 3 # sublets his apartment to 3 people
    subletter_rent = 400 # each pay $400 per month
    total_income_per_month = num_subletters * subletter_rent

    # L2
    months_per_year = 12 # WK
    total_income_per_year = total_income_per_month * months_per_year

    # L3
    john_rent_per_month = 900 # rents the apartment for $900 a month
    total_rent_per_year = months_per_year * john_rent_per_month

    # L4
    profit = total_income_per_year - total_rent_per_year

    # FA
    answer = profit
    return answer