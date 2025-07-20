def solve():
    """Index: 6381.
    Returns: the height of the toy poodle in inches.
    """
    # L1
    standard_poodle_height = 28 # standard poodle in 28 inches tall
    standard_taller_than_miniature = 8 # standard poodle is 8 inches taller than the miniature poodle
    miniature_poodle_height = standard_poodle_height - standard_taller_than_miniature

    # L2
    miniature_taller_than_toy = 6 # miniature poodle is 6 inches taller than the toy poodle
    toy_poodle_height = miniature_poodle_height - miniature_taller_than_toy

    # FA
    answer = toy_poodle_height
    return answer