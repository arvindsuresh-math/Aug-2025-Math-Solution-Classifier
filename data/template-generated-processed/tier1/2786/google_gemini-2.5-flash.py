def solve():
    """Index: 2786.
    Returns: the total cost Tom would have to pay for help with crossing the lake back and forth.
    """
    # L1
    time_one_direction = 4 # takes 4 hours
    num_crossings = 2 # back and forth
    total_crossing_time = time_one_direction * num_crossings

    # L2
    assistant_hourly_cost = 10 # $10 per hour
    total_cost = total_crossing_time * assistant_hourly_cost

    # FA
    answer = total_cost
    return answer