def solve():
    """Index: 6768.
    Returns: the length of Kate's hair in inches.
    """
    # L1
    logan_hair_length = 20 # If Logan hair is 20 inches
    length_difference = 6 # Emily
    emily_hair_length = logan_hair_length - length_difference

    # L2
    kate_divisor = 2 # Kate's hair is half as long
    kate_hair_length = emily_hair_length / kate_divisor

    # FA
    answer = kate_hair_length
    return answer