def solve():
    """Index: 2786.
    Returns: the total cost Tom would have to pay for help crossing the lake back and forth.
    """
    # L1
    hours_one_way = 4 # takes 4 hours (one direction)
    num_crossings = 2 # back and forth
    total_hours = hours_one_way * num_crossings

    # L2
    assistant_rate = 10 # $10 per hour
    total_cost = total_hours * assistant_rate

    # FA
    answer = total_cost
    return answer