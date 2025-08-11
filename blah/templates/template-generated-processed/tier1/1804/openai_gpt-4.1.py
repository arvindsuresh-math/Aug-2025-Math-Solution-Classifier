def solve():
    """Index: 1804.
    Returns: the total number of sides on all the dice Tom and Tim brought.
    """
    # L1
    tom_dice = 4 # Tom brought 4 dice
    tim_dice = 4 # Tim brought 4 dice
    total_dice = tom_dice + tim_dice

    # L2
    sides_per_die = 6 # six-sided dice
    total_sides = total_dice * sides_per_die

    # FA
    answer = total_sides
    return answer