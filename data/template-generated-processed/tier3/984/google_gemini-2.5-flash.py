def solve():
    """Index: 984.
    Returns: the total number of koalas and kangaroos.
    """
    # L1
    kangaroos_per_koala = 5 # 5 kangaroos for each koala
    total_kangaroos = 180 # 180 kangaroos
    num_koalas = total_kangaroos / kangaroos_per_koala

    # L2
    total_animals = num_koalas + total_kangaroos

    # FA
    answer = total_animals
    return answer