def solve():
    """Index: 4700.
    Returns: the total number of stuffed animals the three girls have.
    """
    # L1
    kenley_multiplier = 2 # twice as many as McKenna
    mckenna_animals = 34 # 34 stuffed animals
    kenley_animals = kenley_multiplier * mckenna_animals

    # L2
    tenly_more_than_kenley = 5 # 5 more than Kenley
    tenly_animals = kenley_animals + tenly_more_than_kenley

    # L3
    total_animals = mckenna_animals + kenley_animals + tenly_animals

    # FA
    answer = total_animals
    return answer