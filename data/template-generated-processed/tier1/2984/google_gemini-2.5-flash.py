def solve():
    """Index: 2984.
    Returns: the number of bottles that will not be placed in a crate.
    """
    # L1
    bottles_per_crate = 12 # 12 bottles in each crate
    num_crates = 10 # 10 crates
    bottles_in_crates = bottles_per_crate * num_crates

    # L2
    total_bottles = 130 # a total of 130 bottles
    bottles_not_in_crate = total_bottles - bottles_in_crates

    # FA
    answer = bottles_not_in_crate
    return answer