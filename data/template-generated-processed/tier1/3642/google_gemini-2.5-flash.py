def solve():
    """Index: 3642.
    Returns: the total number of noodles and pirates.
    """
    # L1
    num_pirates = 45 # 45 pirates
    fewer_noodles = 7 # seven fewer noodles
    num_noodles = num_pirates - fewer_noodles

    # L2
    total_noodles_pirates = num_noodles + num_pirates

    # FA
    answer = total_noodles_pirates
    return answer