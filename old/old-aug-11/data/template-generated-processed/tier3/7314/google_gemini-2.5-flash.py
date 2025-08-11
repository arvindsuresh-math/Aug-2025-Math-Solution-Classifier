def solve():
    """Index: 7314.
    Returns: the number of potatoes the chef will have leftover.
    """
    # L1
    fries_needed = 200 # he needs 200 fries
    fries_per_potato = 25 # He can get 25 fries out of 1 potato
    potatoes_needed = fries_needed / fries_per_potato

    # L2
    potatoes_on_hand = 15 # He has 15 potatoes
    leftover_potatoes = potatoes_on_hand - potatoes_needed

    # FA
    answer = leftover_potatoes
    return answer