from fractions import Fraction

def solve():
    """Index: 4156.
    Returns: the total number of gallons Wendy adds to her tanks.
    """
    # L1
    truck_tank_capacity = 20 # 20 gallons
    truck_fill_fraction = 0.5 # half full
    truck_current_gallons = truck_tank_capacity * truck_fill_fraction

    # L2
    car_tank_capacity = 12 # 12 gallons
    car_fill_fraction = Fraction(1, 3) # 1/3 full
    car_current_gallons = car_tank_capacity * car_fill_fraction

    # L3
    gallons_to_add_truck = truck_tank_capacity - truck_current_gallons

    # L4
    gallons_to_add_car = car_tank_capacity - car_current_gallons

    # L5
    total_gallons_to_add = gallons_to_add_truck + gallons_to_add_car

    # FA
    answer = total_gallons_to_add
    return answer