def solve():
    """Index: 3793.
    Returns: the cost per person for the vacation.
    """
    # L1
    airbnb_cost = 3200 # The Airbnb rental costs $3200
    car_rental_cost = 800 # renting a car that will cost $800
    total_rental_cost = airbnb_cost + car_rental_cost

    # L2
    num_people = 8 # vacation for 8 people
    cost_per_person = total_rental_cost / num_people

    # FA
    answer = cost_per_person
    return answer