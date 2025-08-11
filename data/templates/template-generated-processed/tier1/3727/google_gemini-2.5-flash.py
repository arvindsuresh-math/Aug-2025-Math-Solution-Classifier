def solve():
    """Index: 3727.
    Returns: the total number of fried chickens Steph can make.
    """
    # L1
    drumstick_pieces = 24 # 24 pieces of drumstick
    fewer_breast_parts = 4 # 4 fewer breast parts
    breast_parts = drumstick_pieces - fewer_breast_parts

    # L2
    total_fried_chickens = drumstick_pieces + breast_parts

    # FA
    answer = total_fried_chickens
    return answer