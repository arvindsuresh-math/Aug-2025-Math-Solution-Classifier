from fractions import Fraction

def solve():
    """Index: 6585.
    Returns: the number of people who could not take the bus.
    """
    # L1
    carrying_capacity = 80 # carrying capacity of 80 people
    fraction_entered = Fraction(3, 5) # 3/5 of its carrying capacity
    people_entered_first_pickup = fraction_entered * carrying_capacity

    # L2
    available_seats = carrying_capacity - people_entered_first_pickup

    # L3
    people_at_second_pickup = 50 # 50 people at the next pick-up point
    people_could_not_take_bus = people_at_second_pickup - available_seats

    # FA
    answer = people_could_not_take_bus
    return answer