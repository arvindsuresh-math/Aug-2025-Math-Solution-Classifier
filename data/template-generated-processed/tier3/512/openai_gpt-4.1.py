def solve():
    """Index: 512.
    Returns: the number of trips needed for Elysse and her brother to carry all the groceries.
    """
    # L1
    bags_per_trip_per_person = 3 # Elysse can carry 3 bags of groceries into her home with each trip from the car
    number_of_people = 2 # Her brother can carry the same amount
    bags_per_trip_total = bags_per_trip_per_person * number_of_people

    # L2
    total_bags = 30 # 30 bags of groceries
    trips_needed = total_bags / bags_per_trip_total

    # FA
    answer = trips_needed
    return answer