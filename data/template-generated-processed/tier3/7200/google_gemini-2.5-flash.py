def solve():
    """Index: 7200.
    Returns: the total number of turtles Owen had.
    """
    # L1
    owen_initial_turtles = 21 # Owen bred 21 turtles
    johanna_fewer_turtles = 5 # Johanna has 5 fewer turtles than Owen
    johanna_initial_turtles = owen_initial_turtles - johanna_fewer_turtles

    # L2
    owen_multiplier = 2 # Owen has twice as many turtles as before
    owen_turtles_after_month = owen_initial_turtles * owen_multiplier

    # L3
    johanna_loss_divisor = 2 # Johanna loses half of her turtles
    johanna_turtles_after_loss = johanna_initial_turtles / johanna_loss_divisor

    # L4
    owen_total_turtles = owen_turtles_after_month + johanna_turtles_after_loss

    # FA
    answer = owen_total_turtles
    return answer