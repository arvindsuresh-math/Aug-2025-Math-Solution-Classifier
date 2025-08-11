from fractions import Fraction

def solve():
    """Index: 790.
    Returns: the total area of the triangular houses made by Zion and his friends.
    """
    # L1
    base_measurement = 40 # base having a measurement of 40 centimeters
    height_measurement = 20 # height of 20 centimeters
    triangle_area_factor = Fraction(1, 2) # 1/2 base*height
    zion_house_area = triangle_area_factor * base_measurement * height_measurement

    # L2
    friends_houses_area = zion_house_area + zion_house_area

    # L3
    total_combined_area = friends_houses_area + zion_house_area

    # FA
    answer = total_combined_area
    return answer