def solve():
    """Index: 6981.
    Returns: the number of pieces of candy in one bowl.
    """
    # L1
    initial_candy = 100 # Boris has 100 pieces of Halloween candy
    daughter_eats = 8 # His daughter eats 8 pieces of candy
    remaining_candy_after_daughter = initial_candy - daughter_eats

    # L2
    num_bowls = 4 # into 4 different bowls
    candy_per_bowl_initial = remaining_candy_after_daughter / num_bowls

    # L3
    boris_takes = 3 # he takes away 3 pieces of candy from each bowl
    final_candy_per_bowl = candy_per_bowl_initial - boris_takes

    # FA
    answer = final_candy_per_bowl
    return answer