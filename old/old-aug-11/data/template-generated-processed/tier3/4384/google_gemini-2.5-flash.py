from fractions import Fraction

def solve():
    """Index: 4384.
    Returns: the speed of the spaceship in km/hr when there are 400 people on board.
    """
    # L1
    initial_speed = 500 # speed of the spaceship with 200 people on board is 500km per hour
    additional_people_increment = 100 # For every 100 additional people
    speed_reduction_factor = Fraction(1, 2) # speed is halved
    speed_after_first_addition = speed_reduction_factor * initial_speed

    # L2
    total_additional_people = 200 # when there are 400 people on board
    speed_after_second_addition = speed_reduction_factor * speed_after_first_addition

    # FA
    answer = speed_after_second_addition
    return answer