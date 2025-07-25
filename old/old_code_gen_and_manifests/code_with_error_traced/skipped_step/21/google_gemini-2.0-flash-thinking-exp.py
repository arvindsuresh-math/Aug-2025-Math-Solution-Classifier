def solve(
    beetles_per_bird: int = 12, # Each bird eats 12 beetles per day
    birds_per_snake: int = 3, # each snake eats 3 birds per day
    snakes_per_jaguar: int = 5, # and each jaguar eats 5 snakes per day
    num_jaguars: int = 6 # If there are 6 jaguars in a forest
):
    """Index: 21.
    Returns: the total number of beetles eaten each day.
    """

    #: L1
    total_snakes_eaten = snakes_per_jaguar * num_jaguars # eval: 30 = 5 * 6

    #: L2

    #: L3
    total_beetles_eaten = birds_per_snake * beetles_per_bird # eval: 36 = 3 * 12

    #: FA
    answer = total_beetles_eaten
    return answer # eval: return 36
