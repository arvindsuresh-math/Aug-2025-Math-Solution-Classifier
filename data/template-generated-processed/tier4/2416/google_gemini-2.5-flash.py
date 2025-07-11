def solve():
    """Index: 2416.
    Returns: the percentage of hair decorations that are bobby pins, rounded to the nearest percent.
    """
    # L1
    num_barrettes = 6 # 6 barrettes
    scrunchies_multiplier = 2 # twice as many scrunchies as barrettes
    num_scrunchies = num_barrettes * scrunchies_multiplier

    # L2
    bobby_pins_fewer = 3 # three fewer bobby pins than barrettes
    num_bobby_pins = num_barrettes - bobby_pins_fewer

    # L3
    total_decorations = num_barrettes + num_scrunchies + num_bobby_pins

    # L4
    percent_multiplier = 100 # WK
    bobby_pins_percentage_raw = num_bobby_pins / total_decorations * percent_multiplier
    bobby_pins_percentage = round(bobby_pins_percentage_raw)

    # FA
    answer = bobby_pins_percentage
    return answer