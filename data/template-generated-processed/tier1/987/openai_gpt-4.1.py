def solve():
    """Index: 987.
    Returns: the amount of money Linda had at the beginning.
    """
    # L1
    lucy_original = 20 # Lucy originally had $20
    transfer = 5 # Lucy would give Linda $5
    lucy_after = lucy_original - transfer

    # L2
    linda_after = lucy_after # Lucy would have the same amount as Linda
    linda_beginning = linda_after - transfer

    # FA
    answer = linda_beginning
    return answer