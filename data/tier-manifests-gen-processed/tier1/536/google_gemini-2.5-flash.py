def solve():
    """Index: 536.
    Returns: the total number of votes cast.
    """
    # L1
    witch_cake_votes = 7 # 7 people voted for the witch cake
    unicorn_multiplier = 3 # three times as many people voted for the unicorn cake
    unicorn_cake_votes = witch_cake_votes * unicorn_multiplier

    # L2
    dragon_cake_more_than_witch = 25 # 25 more than the number of votes for the witch cake
    dragon_cake_votes = dragon_cake_more_than_witch + witch_cake_votes

    # L3
    total_votes = unicorn_cake_votes + dragon_cake_votes + witch_cake_votes

    # FA
    answer = total_votes
    return answer