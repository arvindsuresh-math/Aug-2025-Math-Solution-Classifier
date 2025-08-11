def solve():
    """Index: 4523.
    Returns: the number of people the alien took to his home planet.
    """
    # L1
    total_abducted = 200 # abducts 200 people
    returned_percentage = 0.8 # returns 80% of the people abducted
    returned_people = total_abducted * returned_percentage

    # L2
    remaining_after_return = total_abducted - returned_people

    # L3
    taken_to_another_planet = 10 # takes 10 people to another planet
    taken_to_home_planet = remaining_after_return - taken_to_another_planet

    # FA
    answer = taken_to_home_planet
    return answer