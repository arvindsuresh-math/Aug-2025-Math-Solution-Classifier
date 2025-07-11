def solve():
    """Index: 536.
    Returns: the total number of votes cast in the baking contest.
    """
    # L1
    witch_votes = 7 # 7 people voted for the witch cake
    unicorn_multiplier = 3 # three times as many people voted for the unicorn cake
    unicorn_votes = witch_votes * unicorn_multiplier

    # L2
    dragon_more_than_witch = 25 # the number of votes for the dragon cake was 25 more than the number of votes for the witch cake
    dragon_votes = dragon_more_than_witch + witch_votes

    # L3
    total_votes = unicorn_votes + dragon_votes + witch_votes

    # FA
    answer = total_votes
    return answer