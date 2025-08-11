def solve():
    """Index: 605.
    Returns: the total number of dice Ivan and Jerry have altogether.
    """
    # L1
    ivan_dice = 20 # Ivan has 20 dice
    multiplier_for_twice = 2 # twice as many dice
    jerry_dice = multiplier_for_twice * ivan_dice

    # L2
    total_dice = ivan_dice + jerry_dice

    # FA
    answer = total_dice
    return answer