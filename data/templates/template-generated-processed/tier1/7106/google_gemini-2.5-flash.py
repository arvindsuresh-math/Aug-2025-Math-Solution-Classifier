def solve():
    """Index: 7106.
    Returns: the number of new shirts Ben has.
    """
    # L1
    alex_shirts = 4 # Alex has 4 new shirts
    joe_more_than_alex = 3 # Joe has 3 more new shirts than Alex
    joe_shirts = alex_shirts + joe_more_than_alex

    # L2
    ben_more_than_joe = 8 # Ben has eight more new shirts than Joe
    ben_shirts = ben_more_than_joe + joe_shirts

    # FA
    answer = ben_shirts
    return answer