def solve():
    """Index: 237.
    Returns: the number of eggs that the 6 other egg hunters collected.
    """
    # L1
    emma_second_round_eggs = 60 # Emma gathered 60 eggs in the second egg hunt round
    tank_second_round_eggs = emma_second_round_eggs / 2

    # L2
    emma_and_tank_second_round_eggs = emma_second_round_eggs + tank_second_round_eggs

    # L3
    tank_second_round_less = 20 # Tank's total number of eggs in the second round was 20 less than the number she had gathered in the first round
    tank_first_round_eggs = tank_second_round_eggs + tank_second_round_less

    # L4
    tank_first_round_more = 10 # Tank gathered 10 more Easter eggs than Emma in their first round of egg hunt
    emma_first_round_eggs = tank_first_round_eggs - tank_first_round_more

    # L5
    emma_and_tank_first_round_eggs = emma_first_round_eggs + tank_first_round_eggs

    # L6
    total_emma_and_tank_eggs = emma_and_tank_first_round_eggs + emma_and_tank_second_round_eggs

    # L7
    total_eggs = 400 # total number of eggs in the pile they were collecting with 6 other people was 400 eggs
    other_hunters_eggs = total_eggs - total_emma_and_tank_eggs

    # FA
    answer = other_hunters_eggs
    return answer