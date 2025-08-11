def solve():
    """Index: 4519.
    Returns: the number of buttons Mari made.
    """
    # L1
    sue_buttons = 6 # Sue made 6 buttons
    multiplier_half = 2 # half as many as Kendra (implies Kendra made twice as many as Sue)
    kendra_buttons = multiplier_half * sue_buttons

    # L2
    mari_more = 4 # 4 more than five times
    mari_multiplier = 5 # five times as many
    mari_buttons = mari_more + mari_multiplier * kendra_buttons

    # FA
    answer = mari_buttons
    return answer