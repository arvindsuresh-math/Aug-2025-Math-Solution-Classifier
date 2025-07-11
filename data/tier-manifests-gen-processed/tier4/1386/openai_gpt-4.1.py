def solve():
    """Index: 1386.
    Returns: the number of customers who did not want their tires changing.
    """
    # L1
    initial_cars = 4 # four cars in the shop already
    new_customers = 6 # another six customers come into the shop
    total_cars = initial_cars + new_customers

    # L2
    tires_per_car = 4 # 4 tires per car
    total_tires_bought = total_cars * tires_per_car

    # L3
    half_fraction = 0.5 # only want half the tires changing
    tires_left_per_half_customer = tires_per_car * half_fraction

    # L4
    num_half_customers = 2 # two customers only want half the tires changing
    tires_left_from_half_customers = tires_left_per_half_customer * num_half_customers

    # L5
    tires_left_end = 20 # 20 tires left at the end of the week
    tires_left_from_no_change = tires_left_end - tires_left_from_half_customers

    # L6
    tires_per_no_change_customer = 4 # 4 tires per customer
    num_no_change_customers = tires_left_from_no_change / tires_per_no_change_customer

    # FA
    answer = num_no_change_customers
    return answer