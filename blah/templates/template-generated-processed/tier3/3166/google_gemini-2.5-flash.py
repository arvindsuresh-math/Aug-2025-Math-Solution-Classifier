def solve():
    """Index: 3166.
    Returns: the number of pictures Louise hung vertically.
    """
    # L1
    total_pictures = 30 # 30 of her pictures
    horizontal_divisor = 2 # half of them horizontally
    horizontal_pictures = total_pictures / horizontal_divisor

    # L2
    haphazard_pictures = 5 # the remaining 5 pictures haphazardly
    horizontal_and_haphazard_pictures = horizontal_pictures + haphazard_pictures

    # L3
    vertical_pictures = total_pictures - horizontal_and_haphazard_pictures

    # FA
    answer = vertical_pictures
    return answer