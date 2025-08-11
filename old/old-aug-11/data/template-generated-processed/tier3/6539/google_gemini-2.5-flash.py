def solve():
    """Index: 6539.
    Returns: the number of cars the fourth and fifth suppliers each receive.
    """
    # L1
    first_supplier_cars = 1000000 # The first supplier receives 1 000 000 cars each.
    additional_cars_second_supplier = 500000 # The second supplier receives 500 000 cars more
    second_supplier_cars = first_supplier_cars + additional_cars_second_supplier

    # L2
    third_supplier_cars = first_supplier_cars + second_supplier_cars

    # L3
    total_cars_first_three_suppliers = first_supplier_cars + second_supplier_cars + third_supplier_cars

    # L4
    total_production = 5650000 # American carmakers produce 5 650 000 cars each year.
    remaining_cars = total_production - total_cars_first_three_suppliers

    # L5
    num_remaining_suppliers = 2 # The fourth and the fifth supplier receive an equal number of cars.
    cars_per_remaining_supplier = remaining_cars / num_remaining_suppliers

    # FA
    answer = cars_per_remaining_supplier
    return answer