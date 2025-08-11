def solve():
    """Index: 1386.
    Returns: the number of customers who did not want their tires changing.
    """
    # L1
    initial_cars_in_shop = 4 # four cars in the shop already
    new_customers_cars = 6 # another six customers come into the shop throughout the week
    total_cars = initial_cars_in_shop + new_customers_cars

    # L2
    tires_per_car = 4 # WK
    total_tires_bought = total_cars * tires_per_car

    # L3
    half_change_fraction = 0.5 # half the tires changing
    tires_left_over_per_half_change_customer = tires_per_car * half_change_fraction

    # L4
    num_half_change_customers = 2 # two customers decide they only want half the tires changing
    total_tires_left_from_half_change_customers = tires_left_over_per_half_change_customer * num_half_change_customers

    # L5
    tires_left_at_end = 20 # shop has 20 tires left at the end of the week
    tires_left_from_no_change_customers = tires_left_at_end - total_tires_left_from_half_change_customers

    # L6
    num_no_change_customers = tires_left_from_no_change_customers / tires_per_car

    # FA
    answer = num_no_change_customers
    return answer