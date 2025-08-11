def solve():
    """Index: 3641.
    Returns: the number of pancakes Bobby has left.
    """
    # L1
    bobby_ate = 5 # he ate 5 pancakes
    dog_ate = 7 # his dog jumped up and was able to eat 7
    total_eaten = bobby_ate + dog_ate

    # L2
    recipe_makes = 21 # The recipe on the box makes 21 pancakes
    pancakes_left = recipe_makes - total_eaten

    # FA
    answer = pancakes_left
    return answer