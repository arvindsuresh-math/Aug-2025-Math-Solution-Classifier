def solve():
    """Index: 7229.
    Returns: the number of new shirts Alex has.
    """
    # L1
    ben_shirts = 15 # If Ben has 15 new shirts
    ben_more_than_joe = 8 # eight more new shirts than Joe
    joe_shirts = ben_shirts - ben_more_than_joe

    # L2
    joe_more_than_alex = 3 # Joe has 3 more new shirts than Alex
    alex_shirts = joe_shirts - joe_more_than_alex

    # FA
    answer = alex_shirts
    return answer