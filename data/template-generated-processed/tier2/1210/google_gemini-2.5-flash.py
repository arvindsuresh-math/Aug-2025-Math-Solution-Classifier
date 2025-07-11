def solve():
    """Index: 1210.
    Returns: the total number of hatchlings produced by the turtles.
    """
    # L1
    eggs_per_clutch = 20 # Each turtle lays a clutch of 20 eggs
    hatch_percentage_num = 40 # 40% of the eggs successfully hatch
    percent_factor = 0.01 # WK
    hatched_eggs_per_turtle = eggs_per_clutch * hatch_percentage_num * percent_factor

    # L2
    num_turtles = 6 # 6 turtles
    total_hatchlings = hatched_eggs_per_turtle * num_turtles

    # FA
    answer = total_hatchlings
    return answer