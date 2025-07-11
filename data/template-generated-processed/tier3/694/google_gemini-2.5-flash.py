def solve():
    """Index: 694.
    Returns: the number of engines that are not defective.
    """
    # L1
    engines_per_batch = 80 # 80 engines each
    num_batches = 5 # 5 batches
    total_engines = engines_per_batch * num_batches

    # L2
    defective_denominator = 4 # one fourth of the engines
    defective_engines = total_engines / defective_denominator

    # L3
    non_defective_engines = total_engines - defective_engines

    # FA
    answer = non_defective_engines
    return answer