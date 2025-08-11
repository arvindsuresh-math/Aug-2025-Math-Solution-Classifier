def solve():
    """Index: 237.
    Returns: the number of eggs collected by the 6 other egg hunters.
    """
    # L1
    emma_second_round_eggs = 60 # Emma gathered 60 eggs in the second egg hunt round
    twice_as_many_divisor = 2 # Emma gathered twice as many eggs as Tank
    tank_second_round_eggs = emma_second_round_eggs / twice_as_many_divisor

    # L2
    total_second_round_eggs = emma_second_round_eggs + tank_second_round_eggs

    # L3
    less_than_first_round = 20 # Tank's total number of eggs in the second round was 20 less than the number she had gathered in the first round
    tank_first_round_eggs = tank_second_round_eggs + less_than_first_round

    # L4
    tank_more_than_emma = 10 # Tank gathered 10 more Easter eggs than Emma
    emma_first_round_eggs = tank_first_round_eggs - tank_more_than_emma

    # L5
    total_first_round_eggs = emma_first_round_eggs + tank_first_round_eggs

    # L6
    total_emma_tank_eggs = total_second_round_eggs + total_first_round_eggs

    # L7
    total_pile_eggs = 400 # If the total number of eggs in the pile they were collecting with 6 other people was 400 eggs
    other_hunters_eggs = total_pile_eggs - total_emma_tank_eggs

    # FA
    answer = other_hunters_eggs
    return answer