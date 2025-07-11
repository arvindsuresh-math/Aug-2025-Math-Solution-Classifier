def solve():
    """Index: 1798.
    Returns: John's current bench press weight after injury and training.
    """
    # L1
    initial_bench = 500 # started with a 500-pound bench press
    percent_lost = 0.8 # bench press goes down 80%
    weight_lost = initial_bench * percent_lost

    # L2
    post_injury_bench = initial_bench - weight_lost

    # L3
    training_factor = 3 # manages to triple the weight
    final_bench = post_injury_bench * training_factor

    # FA
    answer = final_bench
    return answer