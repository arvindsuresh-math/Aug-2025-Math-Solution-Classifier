def solve(
        beetles_per_bird: int = 12, # Each bird eats 12 beetles per day
        birds_per_snake: int = 3, # each snake eats 3 birds per day
        snakes_per_jaguar: int = 5, # each jaguar eats 5 snakes per day
        num_jaguars: int = 6 # If there are 6 jaguars in a forest
    ):
    """Index: 21.
    Returns: the total number of beetles eaten each day.
    """

    #: L1
    total_snakes_eaten = snakes_per_jaguar * num_jaguars

    #: L2
    total_birds_eaten = total_snakes_eaten * birds_per_snake

    #: L3
    total_beetles_eaten = total_birds_eaten - beetles_per_bird

    #: FA
    answer = total_beetles_eaten
    return answer