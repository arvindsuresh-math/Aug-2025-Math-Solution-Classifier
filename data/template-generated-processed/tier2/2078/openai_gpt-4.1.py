def solve():
    """Index: 2078.
    Returns: the number of female Muscovy ducks.
    """
    # L1
    total_ducks = 40 # 40 ducks in a pond
    muscovy_percent = 0.50 # 50 percent of the ducks are Muscovy
    muscovy_ducks = total_ducks * muscovy_percent

    # L2
    female_muscovy_percent = 0.30 # 30 percent of the Muscovies are female
    female_muscovy_ducks = muscovy_ducks * female_muscovy_percent

    # FA
    answer = female_muscovy_ducks
    return answer