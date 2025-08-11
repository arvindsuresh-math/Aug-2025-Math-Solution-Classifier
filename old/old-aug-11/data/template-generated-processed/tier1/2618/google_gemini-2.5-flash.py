def solve():
    """Index: 2618.
    Returns: the number of sandwiches Michelle has left to give to her other co-workers.
    """
    # L1
    gives_to_one_coworker = 4 # gives 4 sandwiches to one of her co-workers
    multiplier_for_self = 2 # keeps twice this amount for herself
    kept_for_self = gives_to_one_coworker * multiplier_for_self

    # L2
    originally_made = 20 # had originally made 20 sandwiches
    sandwiches_left = originally_made - gives_to_one_coworker - kept_for_self

    # FA
    answer = sandwiches_left
    return answer