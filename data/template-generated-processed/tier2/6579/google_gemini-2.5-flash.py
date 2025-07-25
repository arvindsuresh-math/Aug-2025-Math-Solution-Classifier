def solve():
    """Index: 6579.
    Returns: the number of times Megan was not the lead actress.
    """
    # L1
    total_plays = 100 # participated in 100 plays
    lead_actress_percentage_num = 80 # lead actress in 80% of her work
    percent_factor = 0.01 # WK
    lead_actress_plays = total_plays * lead_actress_percentage_num * percent_factor

    # L2
    not_lead_actress_plays = total_plays - lead_actress_plays

    # FA
    answer = not_lead_actress_plays
    return answer