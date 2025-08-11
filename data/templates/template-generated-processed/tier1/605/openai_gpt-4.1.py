def solve():
    """Index: 605.
    Returns: the total number of dice Ivan and Jerry have altogether.
    """
    # L1
    ivan_dice = 20 # Ivan has 20 dice
    jerry_multiplier = 2 # Jerry has twice as many dice as Ivan
    jerry_dice = jerry_multiplier * ivan_dice

    # L2
    total_dice = ivan_dice + jerry_dice

    # FA
    answer = total_dice
    return answer