def solve():
    """Index: 6363.
    Returns: the height the player must be able to jump to dunk a basketball.
    """
    # L1
    rim_height_feet = 10 # The rim of a standard basketball hoop is 10 feet above the ground
    inches_per_foot = 12 # WK
    rim_height_inches = rim_height_feet * inches_per_foot

    # L2
    inches_above_rim_needed = 6 # reach at least 6 inches above the rim
    total_reach_needed = rim_height_inches + inches_above_rim_needed

    # L3
    player_height_feet = 6 # player is 6 feet tall
    reach_above_head = 22 # can reach 22 inches above their head
    player_standing_reach = player_height_feet * inches_per_foot + reach_above_head

    # L4
    jump_height_needed = total_reach_needed - player_standing_reach

    # FA
    answer = jump_height_needed
    return answer