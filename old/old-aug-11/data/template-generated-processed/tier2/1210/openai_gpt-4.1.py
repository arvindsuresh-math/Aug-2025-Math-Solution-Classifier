def solve():
    """Index: 1210.
    Returns: the number of hatchlings produced by 6 turtles.
    """
    # L1
    eggs_per_turtle = 20 # Each turtle lays a clutch of 20 eggs
    hatch_percent_num = 40 # 40% of the eggs successfully hatch
    percent_factor = 0.01 # WK
    eggs_hatched_per_turtle = eggs_per_turtle * hatch_percent_num * percent_factor

    # L2
    num_turtles = 6 # 6 turtles
    total_hatchlings = eggs_hatched_per_turtle * num_turtles

    # FA
    answer = total_hatchlings
    return answer