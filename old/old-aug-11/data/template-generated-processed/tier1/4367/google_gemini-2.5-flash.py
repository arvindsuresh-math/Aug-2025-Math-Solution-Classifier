def solve():
    """Index: 4367.
    Returns: the number of spaces Susan has to move to reach the ending space.
    """
    # L1
    first_turn_move = 8 # moves forward eight spaces
    second_turn_move = 2 # moves two spaces
    second_turn_penalty = 5 # sends her back five spaces
    third_turn_move = 6 # moves forward six more spaces
    total_moved_first_three_turns = first_turn_move + second_turn_move - second_turn_penalty + third_turn_move

    # L2
    total_spaces_game = 48 # 48 spaces from the starting space to the winning end space
    remaining_spaces = total_spaces_game - total_moved_first_three_turns

    # FA
    answer = remaining_spaces
    return answer