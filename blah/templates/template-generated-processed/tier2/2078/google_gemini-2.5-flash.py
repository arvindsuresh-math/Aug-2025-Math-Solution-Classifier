def solve():
    """Index: 2078.
    Returns: the number of female Muscovy ducks.
    """
    # L1
    total_ducks = 40 # 40 ducks in a pond
    muscovy_percent_decimal = 0.50 # 50 percent of the ducks are Muscovy
    num_muscovy_ducks = total_ducks * muscovy_percent_decimal

    # L2
    female_muscovy_percent_decimal = 0.30 # 30 percent of the Muscovies are female
    num_female_muscovy_ducks = num_muscovy_ducks * female_muscovy_percent_decimal

    # FA
    answer = num_female_muscovy_ducks
    return answer