def solve():
    """Index: 6593.
    Returns: the total number of passengers that would fill up 3 trains.
    """
    # L1
    initial_seats_per_carriage = 25 # each carriage has 25 seats
    additional_seats_per_carriage = 10 # accommodate 10 more passengers
    new_seats_per_carriage = initial_seats_per_carriage + additional_seats_per_carriage

    # L2
    carriages_per_train = 4 # 4 carriages in a train
    seats_per_train = new_seats_per_carriage * carriages_per_train

    # L3
    num_trains = 3 # 3 trains
    total_passengers = num_trains * seats_per_train

    # FA
    answer = total_passengers
    return answer