def solve():
    """Index: 512.
    Returns: the total number of trips required to carry the groceries.
    """
    # L1
    bags_per_person_per_trip = 3 # Elysse can carry 3 bags
    number_of_people = 2 # Elysse and her brother
    total_bags_per_trip = bags_per_person_per_trip * number_of_people

    # L2
    total_bags = 30 # 30 bags of groceries
    total_trips = total_bags / total_bags_per_trip

    # FA
    answer = total_trips
    return answer