def solve():
    """Index: 7078.
    Returns: the total number of pieces of bread thrown in the pond.
    """
    # L1
    pieces_left_final = 30 # 30 pieces of bread left in the water
    duck3_ate = 7 # the last duck eats 7 pieces of bread
    duck2_ate = 13 # Another duck eats only 13 pieces of the bread
    pieces_before_first_duck_ate = pieces_left_final + duck3_ate + duck2_ate

    # L2
    half_factor = 2 # One duck eats half of all the pieces of bread
    total_bread_thrown = pieces_before_first_duck_ate * half_factor

    # FA
    answer = total_bread_thrown
    return answer