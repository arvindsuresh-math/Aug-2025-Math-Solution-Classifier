def solve():
    """Index: 563.
    Returns: the number of times the roller coaster will have to run.
    """
    # L1
    num_cars = 7 # 7 cars
    seats_per_car = 2 # each car seats 2 people
    people_per_run = num_cars * seats_per_car

    # L2
    total_people = 84 # 84 people waiting in line
    num_runs = total_people / people_per_run

    # FA
    answer = num_runs
    return answer