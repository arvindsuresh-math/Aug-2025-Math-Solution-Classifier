def solve():
    """Index: 4938.
    Returns: the total number of cartons accepted by the customers.
    """
    # L1
    total_cartons = 400 # 400 cartons of milk
    num_customers = 4 # four of its customers
    cartons_per_customer = total_cartons / num_customers

    # L2
    damaged_cartons_per_customer = 60 # returned 60 cartons damaged
    accepted_cartons_per_customer = cartons_per_customer - damaged_cartons_per_customer

    # L3
    total_accepted_cartons = accepted_cartons_per_customer * num_customers

    # FA
    answer = total_accepted_cartons
    return answer