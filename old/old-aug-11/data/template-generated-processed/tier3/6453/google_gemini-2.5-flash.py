def solve():
    """Index: 6453.
    Returns: the total number of avocados needed.
    """
    # L1
    people_per_batch = 6 # serves about 6 people
    total_people = 42 # 42 people are going to be at the party
    num_batches = total_people / people_per_batch

    # L2
    avocados_per_batch = 4 # Each batch requires 4 avocados
    total_avocados = avocados_per_batch * num_batches

    # FA
    answer = total_avocados
    return answer