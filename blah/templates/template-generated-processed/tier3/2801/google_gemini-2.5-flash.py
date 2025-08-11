def solve():
    """Index: 2801.
    Returns: the number of tarantulas Borgnine needs to see.
    """
    # L1
    num_chimps = 12 # 12 chimps
    chimp_legs = 4 # WK
    chimp_legs_total = num_chimps * chimp_legs

    # L2
    num_lions = 8 # 8 lions
    lion_legs = 4 # WK
    lion_legs_total = num_lions * lion_legs

    # L3
    num_lizards = 5 # 5 lizards
    lizard_legs = 4 # WK
    lizard_legs_total = num_lizards * lizard_legs

    # L4
    total_legs_seen = chimp_legs_total + lion_legs_total + lizard_legs_total

    # L5
    goal_legs = 1100 # 1100 legs
    tarantula_legs_needed = goal_legs - total_legs_seen

    # L6
    tarantula_legs = 8 # WK
    num_tarantulas = tarantula_legs_needed / tarantula_legs

    # FA
    answer = num_tarantulas
    return answer