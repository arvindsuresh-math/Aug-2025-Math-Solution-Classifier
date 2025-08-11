from fractions import Fraction

def solve():
    """Index: 6024.
    Returns: the total number of water bottles Ellis' family will need.
    """
    # L1
    travel_time_one_way = 8 # 8 hours
    total_travel_hours = travel_time_one_way + travel_time_one_way

    # L2
    water_per_person_per_hour = Fraction(1, 2) # 1/2 a bottle of water
    bottles_per_person_total = water_per_person_per_hour * total_travel_hours

    # L3
    travelers = 4 # four people total
    total_water_bottles_needed = bottles_per_person_total * travelers

    # FA
    answer = total_water_bottles_needed
    return answer