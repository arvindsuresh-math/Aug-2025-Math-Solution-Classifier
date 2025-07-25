def solve():
    """Index: 1907.
    Returns: the length of the smallest model mustang in inches.
    """
    # L1
    full_size_mustang_length = 240 # A full size mustang is 240 inches long
    mid_size_divisor = 10 # 1/10th the size
    mid_size_model_length = full_size_mustang_length / mid_size_divisor

    # L2
    smallest_model_divisor = 2 # half the size of the mid-size model
    smallest_model_length = mid_size_model_length / smallest_model_divisor

    # FA
    answer = smallest_model_length
    return answer