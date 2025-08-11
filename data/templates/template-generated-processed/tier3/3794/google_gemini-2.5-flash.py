def solve():
    """Index: 3794.
    Returns: the number of buttons Sue made.
    """
    # L1
    Mari_buttons = 8 # Mari made 8 buttons
    kendra_multiplier = 5 # five times as many
    kendra_addition = 4 # 4 more than
    kendra_buttons = kendra_addition + kendra_multiplier * Mari_buttons

    # L2
    sue_divisor = 2 # half as many as Kendra
    sue_buttons = kendra_buttons / sue_divisor

    # FA
    answer = sue_buttons
    return answer