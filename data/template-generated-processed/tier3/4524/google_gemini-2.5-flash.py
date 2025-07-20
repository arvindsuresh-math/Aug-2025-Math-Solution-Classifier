def solve():
    """Index: 4524.
    Returns: the number of oranges Johann has now.
    """
    # L1
    initial_oranges = 60 # Johann had 60 oranges
    eaten_oranges = 10 # He decided to eat 10
    oranges_after_eating = initial_oranges - eaten_oranges

    # L2
    stolen_divisor = 2 # half were stolen by Carson
    stolen_oranges = oranges_after_eating / stolen_divisor

    # L3
    returned_oranges = 5 # Carson returned exactly 5
    final_oranges = stolen_oranges + returned_oranges

    # FA
    answer = final_oranges
    return answer