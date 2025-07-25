def solve():
    """Index: 2120.
    Returns: the total difference in pins knocked down between Richard and Patrick.
    """
    # L1
    patrick_pins_r1 = 70 # Patrick knocked down a total of 70 pins
    richard_more_than_patrick_r1 = 15 # Richard knocked down 15 more pins than Patrick
    richard_pins_r1 = patrick_pins_r1 + richard_more_than_patrick_r1

    # L2
    patrick_multiplier_r2 = 2 # Patrick knocked down twice as many pins as Richard in the first round
    patrick_pins_r2 = richard_pins_r1 * patrick_multiplier_r2

    # L3
    richard_less_than_patrick_r2 = 3 # Richard knocked down 3 less than Patrick
    richard_pins_r2 = patrick_pins_r2 - richard_less_than_patrick_r2

    # L4
    total_patrick_pins = patrick_pins_r1 + patrick_pins_r2

    # L5
    total_richard_pins = richard_pins_r1 + richard_pins_r2

    # L6
    difference_in_pins = total_richard_pins - total_patrick_pins

    # FA
    answer = difference_in_pins
    return answer