def solve():
    """Index: 3349.
    Returns: the number of square feet in Nada's house.
    """
    # L3
    sara_house_size = 1000 # Sara's house is 1000 square feet
    sara_house_larger_than_twice_nada = 100 # 100 square feet larger than 2 times Nada's house
    multiplier_for_nada = 2 # 2 times Nada's house
    two_times_nada_house = sara_house_size - sara_house_larger_than_twice_nada

    # L4
    nada_house_size = two_times_nada_house / multiplier_for_nada

    # FA
    answer = nada_house_size
    return answer