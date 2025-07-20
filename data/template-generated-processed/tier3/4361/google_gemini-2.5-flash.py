def solve():
    """Index: 4361.
    Returns: the number of tripodasauruses in the flock.
    """
    # L1
    heads_per_animal = 1 # Each animal has 1 head (implied)
    legs_per_animal = 3 # has three legs
    total_parts_per_animal = heads_per_animal + legs_per_animal

    # L2
    total_heads_and_legs = 20 # total of 20 heads and legs
    num_tripodauruses = total_heads_and_legs / total_parts_per_animal

    # FA
    answer = num_tripodauruses
    return answer