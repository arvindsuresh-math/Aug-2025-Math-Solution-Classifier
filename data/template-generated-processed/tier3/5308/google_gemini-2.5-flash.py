def solve():
    """Index: 5308.
    Returns: the weight of one of Trace's bags in pounds.
    """
    # L1
    gordon_bag_1_weight = 3 # One of Gordon’s shopping bags weighs three pounds
    gordon_bag_2_weight = 7 # and the other weighs seven
    total_gordon_weight = gordon_bag_1_weight + gordon_bag_2_weight

    # L2
    num_trace_bags = 5 # Trace has five shopping bags
    weight_per_trace_bag = total_gordon_weight / num_trace_bags

    # FA
    answer = weight_per_trace_bag
    return answer