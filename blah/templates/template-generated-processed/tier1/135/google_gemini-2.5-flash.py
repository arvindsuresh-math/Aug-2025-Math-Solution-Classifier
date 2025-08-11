def solve():
    """Index: 135.
    Returns: the number of square feet in Benedict's house.
    """
    # L2
    kennedy_house_size = 10000 # Kennedy's house is 10000 square feet
    larger_than_value = 600 # 600 square feet larger than
    coefficient_of_x = 4 # 4 times Benedict's house
    rhs_after_subtraction = kennedy_house_size - larger_than_value

    # L3
    benedict_house_size = rhs_after_subtraction / coefficient_of_x

    # FA
    answer = benedict_house_size
    return answer