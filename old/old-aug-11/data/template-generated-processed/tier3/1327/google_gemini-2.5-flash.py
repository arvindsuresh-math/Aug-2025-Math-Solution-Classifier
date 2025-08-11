def solve():
    """Index: 1327.
    Returns: the distance, in yards, from the starting tee to the hole.
    """
    # L1
    first_turn_distance = 180 # it traveled 180 yards straight toward the hole
    half_divisor = 2 # half as far as it did on his first turn
    second_turn_distance = first_turn_distance / half_divisor

    # L2
    total_distance_after_two_turns = first_turn_distance + second_turn_distance

    # L3
    yards_past_hole = 20 # the ball landed 20 yards beyond the hole
    distance_to_hole = total_distance_after_two_turns - yards_past_hole

    # FA
    answer = distance_to_hole
    return answer