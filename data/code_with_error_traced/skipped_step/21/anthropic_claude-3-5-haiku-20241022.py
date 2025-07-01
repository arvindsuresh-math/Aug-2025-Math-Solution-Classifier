def solve(
        jaguars: int = 6, # If there are 6 jaguars in a forest
        snakes_per_jaguar: int = 5, # each jaguar eats 5 snakes per day
        birds_per_snake: int = 3, # each snake eats 3 birds per day
        beetles_per_bird: int = 12 # each bird eats 12 beetles per day
    ):
    """Index: 21.
    Returns: the total number of beetles eaten each day in the forest."""

    #: L1

    #: L2
    total_birds_eaten = birds_per_snake * birds_per_snake # eval: 9 = 3 * 3

    #: L3
    total_beetles_eaten = total_birds_eaten * beetles_per_bird # eval: 108 = 9 * 12

    #: FA
    answer = total_beetles_eaten
    return answer # eval: return 108
