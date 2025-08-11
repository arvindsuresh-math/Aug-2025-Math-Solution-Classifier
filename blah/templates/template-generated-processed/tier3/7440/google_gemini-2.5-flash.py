def solve():
    """Index: 7440.
    Returns: the number of cupcakes that each of Carla's daughter's friends ate.
    """
    # L1
    initial_cupcakes_per_batch = 65 # Baking in batches of 65 cupcakes
    sampled_cupcakes_per_batch = 5 # took 5 cupcakes from each batch
    cupcakes_per_batch_after_sampling = initial_cupcakes_per_batch - sampled_cupcakes_per_batch

    # L2
    num_batches = 45 # made 45 batches of cupcakes
    total_cupcakes_for_party = num_batches * cupcakes_per_batch_after_sampling

    # L3
    num_friends = 19 # 19 friends
    num_daughter = 1 # including the daughter
    total_people_at_party = num_friends + num_daughter

    # L4
    cupcakes_per_person = total_cupcakes_for_party / total_people_at_party

    # FA
    answer = cupcakes_per_person
    return answer