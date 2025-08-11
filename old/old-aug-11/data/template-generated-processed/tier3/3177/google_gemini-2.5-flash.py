def solve():
    """Index: 3177.
    Returns: the total number of loads of laundry washed that week.
    """
    # L1
    wednesday_loads = 6 # On Wednesday he washed six loads of clothes
    double_factor = 2 # double the number of loads
    thursday_loads = wednesday_loads * double_factor

    # L2
    half_factor = 2 # half of the loads
    friday_loads = thursday_loads / half_factor

    # L3
    third_factor = 3 # a third of the loads
    saturday_loads = wednesday_loads / third_factor

    # L4
    total_loads = wednesday_loads + thursday_loads + friday_loads + saturday_loads

    # FA
    answer = total_loads
    return answer