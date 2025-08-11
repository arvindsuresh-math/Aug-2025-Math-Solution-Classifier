def solve():
    """Index: 5333.
    Returns: the total number of slices and pieces of bell pepper.
    """
    # L1
    num_bell_peppers = 5 # 5 bell peppers
    slices_per_pepper = 20 # 20 large slices
    total_large_slices = num_bell_peppers * slices_per_pepper

    # L2
    half_divisor = 2 # half those slices
    slices_to_cut_smaller = total_large_slices / half_divisor

    # L3
    pieces_per_small_slice = 3 # cuts them into 3 smaller pieces each
    total_small_pieces = slices_to_cut_smaller * pieces_per_small_slice

    # L4
    total_slices_and_pieces = slices_to_cut_smaller + total_small_pieces

    # FA
    answer = total_slices_and_pieces
    return answer