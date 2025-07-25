def solve():
    """Index: 2675.
    Returns: the total number of coins Mrs. Jane gave to the boys.
    """
    # L1
    jayden_coins = 300 # Jayden received 300 coins
    jason_more_than_jayden = 60 # Jason was paid 60 more coins than Jayden
    jason_coins = jayden_coins + jason_more_than_jayden

    # L2
    total_coins = jason_coins + jayden_coins

    # FA
    answer = total_coins
    return answer