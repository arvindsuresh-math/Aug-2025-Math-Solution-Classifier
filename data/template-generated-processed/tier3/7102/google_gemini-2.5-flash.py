def solve():
    """Index: 7102.
    Returns: the area of Bob's garden in square feet.
    """
    # L1
    property_width = 1000 # His land is 1000 feet wide
    garden_width_divisor = 8 # an eighth of the width
    garden_width = property_width / garden_width_divisor

    # L2
    property_length = 2250 # 2250 feet long
    garden_length_divisor = 10 # a tenth of the length
    garden_length = property_length / garden_length_divisor

    # L3
    garden_area = garden_width * garden_length

    # FA
    answer = garden_area
    return answer