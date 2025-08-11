def solve():
    """Index: 5613.
    Returns: the number of pictures the memory card can hold with the new size.
    """
    # L1
    initial_pictures = 3000 # 3,000 pictures
    initial_megabytes_per_picture = 8 # 8 megabytes each
    total_capacity_megabytes = initial_pictures * initial_megabytes_per_picture

    # L2
    new_megabytes_per_picture = 6 # 6 megabytes each
    new_number_of_pictures = total_capacity_megabytes / new_megabytes_per_picture

    # FA
    answer = new_number_of_pictures
    return answer