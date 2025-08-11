from fractions import Fraction

def solve():
    """Index: 791.
    Returns: the number of Dutch Americans who sat at the windows.
    """
    # L1
    total_people_on_bus = 90 # 90 people on William's bus
    dutch_fraction = Fraction(3, 5) # 3/5 were Dutch
    num_dutch_people = dutch_fraction * total_people_on_bus

    # L2
    dutch_american_fraction = Fraction(1, 2) # 1/2 of the Dutch who were also American
    num_dutch_americans = dutch_american_fraction * num_dutch_people

    # L3
    window_seat_fraction = Fraction(1, 3) # 1/3 got window seats
    num_dutch_americans_window_seats = window_seat_fraction * num_dutch_americans

    # FA
    answer = num_dutch_americans_window_seats
    return answer