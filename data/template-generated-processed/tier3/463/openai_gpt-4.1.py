def solve():
    """Index: 463.
    Returns: the total number of hours it would take Camilla to finish making 12 pizzas.
    """
    # L1
    total_pizzas = 12 # Camilla needs 12 pizzas
    pizzas_per_batch = 3 # one batch of pizza dough can make 3 pizzas
    batches_needed = total_pizzas / pizzas_per_batch

    # L2
    dough_time_per_batch = 30 # It takes 30 minutes to make pizza dough
    total_dough_time = batches_needed * dough_time_per_batch

    # L3
    oven_capacity = 2 # the oven can only fit 2 pizzas at a time
    oven_rounds = total_pizzas / oven_capacity

    # L4
    oven_time_per_round = 30 # another 30 minutes in the oven for the pizza to cook
    total_oven_time = oven_rounds * oven_time_per_round

    # L5
    total_minutes = total_dough_time + total_oven_time

    # L6
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer