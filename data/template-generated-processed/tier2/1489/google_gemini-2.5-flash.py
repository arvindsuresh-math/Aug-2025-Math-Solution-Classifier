def solve():
    """Index: 1489.
    Returns: the total pounds lost by the 3 people.
    """
    # L1
    seth_lost_pounds = 17.5 # Seth lost 17.5 pounds

    # L2
    jerome_multiplier = 3 # three times that many pounds
    jerome_lost_pounds = jerome_multiplier * seth_lost_pounds

    # L3
    veronica_more_than_seth = 1.5 # 1.5 pounds more than Seth
    veronica_lost_pounds = seth_lost_pounds + veronica_more_than_seth

    # L4
    total_pounds_lost = seth_lost_pounds + jerome_lost_pounds + veronica_lost_pounds

    # FA
    answer = total_pounds_lost
    return answer