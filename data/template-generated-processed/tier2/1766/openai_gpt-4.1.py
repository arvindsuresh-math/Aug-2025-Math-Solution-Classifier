def solve():
    """Index: 1766.
    Returns: the total number of necklaces made on Sunday.
    """
    # L1
    first_machine_necklaces = 45 # first machine made 45 necklaces
    multiplier = 2.4 # second machine made 2.4 times as many
    second_machine_necklaces = multiplier * first_machine_necklaces

    # L2
    total_necklaces = first_machine_necklaces + second_machine_necklaces

    # FA
    answer = total_necklaces
    return answer