def solve():
    """Index: 6161.
    Returns: how much Emilee earns.
    """
    # L1
    terrence_earnings = 30 # Terrence earns $30
    jermaine_extra = 5 # $5 more than Terrence
    jermaine_earnings = terrence_earnings + jermaine_extra

    # L2
    total_jermaine_terrence = terrence_earnings + jermaine_earnings

    # L3
    total_earnings_all = 90 # total of $90
    emilee_earnings = total_earnings_all - total_jermaine_terrence

    # FA
    answer = emilee_earnings
    return answer