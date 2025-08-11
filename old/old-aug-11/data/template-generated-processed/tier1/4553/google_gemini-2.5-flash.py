def solve():
    """Index: 4553.
    Returns: Angela's height in centimeters.
    """
    # L1
    amy_height = 150 # Amy is 150 cm tall

    # L2
    helen_taller_than_amy = 3 # Helen is 3 cm taller than Amy
    helen_height = amy_height + helen_taller_than_amy

    # L3
    angela_taller_than_helen = 4 # Angela is 4 cm taller than Helen
    angela_height = helen_height + angela_taller_than_helen

    # FA
    answer = angela_height
    return answer