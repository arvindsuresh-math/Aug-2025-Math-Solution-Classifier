from fractions import Fraction

def solve():
    """Index: 6784.
    Returns: the combined capacity of the two buses.
    """
    # L1
    train_capacity = 120 # capacity of 120 people
    bus_capacity_fraction = Fraction(1, 6) # capacity of 1/6 as much as the train
    single_bus_capacity = train_capacity * bus_capacity_fraction

    # L2
    number_of_buses = 2 # two buses
    combined_bus_capacity = single_bus_capacity * number_of_buses

    # FA
    answer = combined_bus_capacity
    return answer