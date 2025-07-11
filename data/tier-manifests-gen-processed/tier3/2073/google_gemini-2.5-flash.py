def solve():
    """Index: 2073.
    Returns: the weight of each pile of jelly beans.
    """
    # L1
    initial_jelly_beans = 36 # Alex had 36 ounces of jelly beans
    eaten_jelly_beans = 6 # He ate 6 ounces
    remaining_jelly_beans = initial_jelly_beans - eaten_jelly_beans

    # L2
    num_piles = 3 # divided the rest equally into 3 piles
    weight_per_pile = remaining_jelly_beans / num_piles

    # FA
    answer = weight_per_pile
    return answer