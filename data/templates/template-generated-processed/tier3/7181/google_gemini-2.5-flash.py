def solve():
    """Index: 7181.
    Returns: the number of unoccupied seats in business class.
    """
    # L1
    economy_class_capacity = 50 # 50 in economy class seating
    economy_class_occupancy_divisor = 2 # economy class is half full
    economy_class_people = economy_class_capacity / economy_class_occupancy_divisor

    # L2
    first_class_people = 3 # only three people on the flight have first class seats
    business_class_people = economy_class_people - first_class_people

    # L3
    business_class_capacity = 30 # 30 in business class
    unoccupied_business_seats = business_class_capacity - business_class_people

    # FA
    answer = unoccupied_business_seats
    return answer