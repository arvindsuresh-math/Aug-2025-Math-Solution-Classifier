from fractions import Fraction

def solve():
    """Index: 4696.
    Returns: the total number of employees in the two buses combined.
    """
    # L1
    first_bus_capacity_percentage = Fraction(60, 100) # 60% of capacity full
    bus_capacity = 150 # capacity of 150
    passengers_first_bus = first_bus_capacity_percentage * bus_capacity

    # L2
    second_bus_capacity_percentage = Fraction(70, 100) # 70% of capacity full
    passengers_second_bus = second_bus_capacity_percentage * bus_capacity

    # L3
    total_employees = passengers_second_bus + passengers_first_bus

    # FA
    answer = total_employees
    return answer