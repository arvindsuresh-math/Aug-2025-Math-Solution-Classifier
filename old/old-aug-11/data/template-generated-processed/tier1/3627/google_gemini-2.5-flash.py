def solve():
    """Index: 3627.
    Returns: the total number of steps Jeffrey takes.
    """
    # L1
    steps_forward_per_cycle = 3 # for every three steps forward
    steps_backward_per_cycle = 2 # he takes two steps backwards
    steps_per_net_step = steps_forward_per_cycle + steps_backward_per_cycle

    # L2
    distance_to_mailbox = 66 # distance between the house and the mailbox is 66 steps
    total_steps = distance_to_mailbox * steps_per_net_step

    # FA
    answer = total_steps
    return answer