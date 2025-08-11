def solve():
    """Index: 3253.
    Returns: the total number of big cats at the feline sanctuary.
    """
    # L1
    lions = 12 # 12 lions
    tigers = 14 # 14 tigers
    cougar_divisor = 2 # half as many cougars
    cougars = (lions + tigers) / cougar_divisor

    # L2
    total_big_cats = lions + tigers + cougars

    # FA
    answer = total_big_cats
    return answer