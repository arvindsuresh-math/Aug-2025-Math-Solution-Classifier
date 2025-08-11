def solve():
    """Index: 3043.
    Returns: the total number of buttons Mark ended up with.
    """
    # L1
    initial_buttons = 14 # Mark started the day with 14 buttons
    shane_multiplier = 3 # 3 times that amount of buttons
    buttons_from_shane = initial_buttons * shane_multiplier

    # L2
    total_buttons_after_shane = buttons_from_shane + initial_buttons

    # L3
    sam_share_divisor = 2 # half of Mark’s buttons
    buttons_given_to_sam = total_buttons_after_shane / sam_share_divisor

    # L4
    final_buttons = buttons_given_to_sam

    # FA
    answer = final_buttons
    return answer