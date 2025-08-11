from fractions import Fraction

def solve():
    """Index: 4907.
    Returns: the total number of units Daleyza was contracted to build.
    """
    # L1
    first_building_units = 4000 # The first building was designed to have 4000 units
    second_building_fraction = Fraction(2, 5) # 2/5 times as many units as the first building
    second_building_units = second_building_fraction * first_building_units

    # L2
    first_and_second_total_units = second_building_units + first_building_units

    # L3
    third_building_percentage = Fraction(120, 100) # 20% more units than the second building
    third_building_units = third_building_percentage * second_building_units

    # L4
    total_contracted_units = first_and_second_total_units + third_building_units

    # FA
    answer = total_contracted_units
    return answer