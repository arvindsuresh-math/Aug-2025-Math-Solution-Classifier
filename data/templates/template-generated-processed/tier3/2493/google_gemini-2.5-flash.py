def solve():
    """Index: 2493.
    Returns: the number of additional eggs Tyler needs to buy.
    """
    # L1
    target_people = 8 # make a cake for eight people
    original_people = 4 # recipe for a four-person cake
    scaling_factor = target_people / original_people

    # L2
    eggs_for_four_people = 2 # requires 2 eggs
    eggs_needed_for_eight_people = eggs_for_four_people * scaling_factor

    # L3
    eggs_tyler_has = 3 # Tyler has 3 eggs in the fridge
    eggs_to_buy = eggs_needed_for_eight_people - eggs_tyler_has

    # FA
    answer = eggs_to_buy
    return answer