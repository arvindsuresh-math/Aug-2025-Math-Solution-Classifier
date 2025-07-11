def solve():
    """Index: 563.
    Returns: the number of times the ride operator must run the roller coaster to give everyone a turn.
    """
    # L1
    cars = 7 # The roller coaster has 7 cars
    seats_per_car = 2 # each car seats 2 people
    people_per_run = cars * seats_per_car

    # L2
    people_in_line = 84 # There are 84 people waiting in line
    runs_needed = people_in_line / people_per_run

    # FA
    answer = runs_needed
    return answer