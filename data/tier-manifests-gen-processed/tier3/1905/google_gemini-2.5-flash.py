def solve():
    """Index: 1905.
    Returns: the number of washers remaining in the bag.
    """
    # L1
    total_pipe_length = 40 # 40 feet of copper pipe
    feet_per_bolt = 5 # every 5 feet of pipe
    num_bolts = total_pipe_length / feet_per_bolt

    # L2
    washers_per_bolt = 2 # for every bolt, he uses two washers
    washers_needed = num_bolts * washers_per_bolt

    # L3
    initial_washers_in_bag = 20 # a bag of 20 washers
    washers_remaining = initial_washers_in_bag - washers_needed

    # FA
    answer = washers_remaining
    return answer