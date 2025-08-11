def solve():
    """Index: 3034.
    Returns: the number of votes Eliot got.
    """
    # L1
    shaun_multiplier = 5 # 5 times as many votes as Randy
    randy_votes = 16 # Randy got 16 votes
    shaun_votes = shaun_multiplier * randy_votes

    # L2
    eliot_multiplier = 2 # twice as many votes as Shaun
    eliot_votes = shaun_votes * eliot_multiplier

    # FA
    answer = eliot_votes
    return answer