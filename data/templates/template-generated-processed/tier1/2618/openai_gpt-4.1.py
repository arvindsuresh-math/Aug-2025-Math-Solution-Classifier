def solve():
    """Index: 2618.
    Returns: the number of sandwiches Michelle has left to give to her other co-workers.
    """
    # L1
    sandwiches_given = 4 # gives 4 sandwiches to one of her co-workers
    multiplier_for_herself = 2 # keeps twice this amount for herself
    sandwiches_kept = sandwiches_given * multiplier_for_herself

    # L2
    total_sandwiches = 20 # she had originally made 20 sandwiches
    sandwiches_left = total_sandwiches - sandwiches_given - sandwiches_kept

    # FA
    answer = sandwiches_left
    return answer