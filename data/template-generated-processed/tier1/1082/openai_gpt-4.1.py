def solve():
    """Index: 1082.
    Returns: the number of tonnes of maize Alfred has at the end of 2 years.
    """
    # L2
    months_per_year = 12 # WK
    years = 2 # next 2 years
    maize_per_month = 1 # a tonne of maize each month
    maize_stored = months_per_year * years * maize_per_month

    # L3
    maize_stolen = 5 # 5 tonnes are stolen
    maize_after_theft = maize_stored - maize_stolen

    # L4
    maize_donation = 8 # 8 tonnes are given to him as a donation
    maize_final = maize_after_theft + maize_donation

    # FA
    answer = maize_final
    return answer