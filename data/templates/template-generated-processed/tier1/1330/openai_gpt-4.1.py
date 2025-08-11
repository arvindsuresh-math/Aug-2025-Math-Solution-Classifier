def solve():
    """Index: 1330.
    Returns: Sara's height in inches.
    """
    # L1
    roy_height = 36 # Roy is 36 inches tall

    # L2
    joe_taller_than_roy = 3 # Joe is 3 inches taller than Roy
    joe_height = joe_taller_than_roy + roy_height

    # L3
    sara_taller_than_joe = 6 # Sara is 6 inches taller than Joe
    sara_height = sara_taller_than_joe + joe_height

    # FA
    answer = sara_height
    return answer