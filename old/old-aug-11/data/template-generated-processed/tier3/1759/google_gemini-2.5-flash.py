from fractions import Fraction

def solve():
    """Index: 1759.
    Returns: the total length of Jason's commute in miles.
    """
    # L1
    distance_1_to_2 = 6 # The distance between the first store and the second store is 6 miles
    additional_fraction = Fraction(2, 3) # 2/3rds longer
    additional_distance_2_to_3 = distance_1_to_2 * additional_fraction

    # L2
    total_distance_2_to_3 = additional_distance_2_to_3 + distance_1_to_2

    # L3
    distance_house_to_1 = 4 # The distance from his house to the first store and the last store to work is the same, 4 miles
    distance_3_to_work = 4 # The distance from his house to the first store and the last store to work is the same, 4 miles
    total_commute_distance = total_distance_2_to_3 + distance_1_to_2 + distance_house_to_1 + distance_3_to_work

    # FA
    answer = total_commute_distance
    return answer