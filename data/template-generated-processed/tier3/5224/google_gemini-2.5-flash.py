def solve():
    """Index: 5224.
    Returns: the weight of each of the remaining statues.
    """
    # L1
    initial_block_weight = 80 # an 80-pound block of marble
    discarded_marble_weight = 22 # weighed 22 pounds
    weight_after_discard = initial_block_weight - discarded_marble_weight

    # L2
    first_statue_weight = 10 # The first statue he carved weighed 10 pounds
    weight_after_first_statue = weight_after_discard - first_statue_weight

    # L3
    second_statue_weight = 18 # The second statue weighed 18
    weight_of_remaining_two_statues = weight_after_first_statue - second_statue_weight

    # L4
    number_of_remaining_statues = 2 # The remaining two statues
    weight_per_remaining_statue = weight_of_remaining_two_statues / number_of_remaining_statues

    # FA
    answer = weight_per_remaining_statue
    return answer