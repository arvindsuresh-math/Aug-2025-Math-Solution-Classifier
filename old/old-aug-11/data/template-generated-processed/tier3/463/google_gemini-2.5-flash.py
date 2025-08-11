def solve():
    """Index: 463.
    Returns: the total time in hours to make 12 pizzas.
    """
    # L1
    total_pizzas_needed = 12 # how many hours would it take for Camilla to finish making 12 pizzas
    pizzas_per_dough_batch = 3 # one batch of pizza dough can make 3 pizzas
    dough_batches_needed = total_pizzas_needed / pizzas_per_dough_batch

    # L2
    dough_making_time_per_batch = 30 # It takes 30 minutes to make pizza dough
    total_dough_making_time = dough_making_time_per_batch * dough_batches_needed

    # L3
    oven_capacity = 2 # the oven can only fit 2 pizzas at a time
    oven_baking_times = total_pizzas_needed / oven_capacity

    # L4
    oven_cook_time_per_batch = 30 # another 30 minutes in the oven for the pizza to cook
    total_oven_baking_time = oven_cook_time_per_batch * oven_baking_times

    # L5
    total_minutes = total_dough_making_time + total_oven_baking_time

    # L6
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer