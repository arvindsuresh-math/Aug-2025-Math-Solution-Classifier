def solve():
    """Index: 2751.
    Returns: the total number of baseball cards the three have.
    """
    # L1
    carlos_cards = 20 # Carlos has 20 baseball cards
    matias_fewer_than_carlos = 6 # 6 fewer cards than Carlos
    matias_cards = carlos_cards - matias_fewer_than_carlos

    # L2
    jorge_cards = matias_cards # Jorge has an equal number of baseball cards as Matias
    total_cards = matias_cards + jorge_cards + carlos_cards

    # FA
    answer = total_cards
    return answer