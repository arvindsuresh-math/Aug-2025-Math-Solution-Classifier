def solve():
    """Index: 1798.
    Returns: John's current bench press weight.
    """
    # L1
    initial_bench_press = 500 # started with a 500-pound bench press
    loss_percent = 0.8 # goes down 80%
    weight_lost = initial_bench_press * loss_percent

    # L2
    bench_after_injury = initial_bench_press - weight_lost

    # L3
    training_multiplier = 3 # triple the weight
    final_bench_press = bench_after_injury * training_multiplier

    # FA
    answer = final_bench_press
    return answer