def solve():
    """Index: 21.
    Returns: the total number of beetles eaten each day in the forest.
    """
    # L1
    snakes_per_jaguar = 5 # each jaguar eats 5 snakes per day
    num_jaguars = 6 # 6 jaguars in a forest
    total_snakes = snakes_per_jaguar * num_jaguars

    # L2
    birds_per_snake = 3 # each snake eats 3 birds per day
    total_birds = total_snakes * birds_per_snake

    # L3
    beetles_per_bird = 12 # each bird eats 12 beetles per day
    total_beetles = total_birds * beetles_per_bird

    # FA
    answer = total_beetles
    return answer