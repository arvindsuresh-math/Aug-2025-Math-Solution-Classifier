def solve():
    """Index: 5949.
    Returns: the number of jars of milk good for sale that week.
    """
    # L1
    initial_cartons = 50 # Logan's father receives 50 cartons delivery
    cartons_less_delivered = 20 # he received 20 cartons less
    remaining_cartons = initial_cartons - cartons_less_delivered

    # L2
    jars_per_carton = 20 # each carton having 20 jars of milk
    total_jars_after_delivery_issue = remaining_cartons * jars_per_carton

    # L3
    jars_damaged_in_partial_carton = 3 # 3 jars in 5 cartons each was damaged
    num_partially_damaged_cartons = 5 # 5 cartons each was damaged
    jars_damaged_from_partial_cartons = jars_damaged_in_partial_carton * num_partially_damaged_cartons

    # L4
    total_damaged_jars = jars_per_carton + jars_damaged_from_partial_cartons

    # L5
    jars_good_for_sale = total_jars_after_delivery_issue - total_damaged_jars

    # FA
    answer = jars_good_for_sale
    return answer