def solve():
    """Index: 7037.
    Returns: the percentage of altered votes for Game of Thrones.
    """
    # L1
    taotd_discard_percent_num = 80 # 80% of the votes for The Art of the Deal
    taotd_initial_votes = 20 # 20 votes for The Art of the Deal
    percent_factor = 0.01 # WK
    taotd_discarded_votes = taotd_discard_percent_num * percent_factor * taotd_initial_votes

    # L2
    taotd_altered_votes = taotd_initial_votes - taotd_discarded_votes

    # L3
    twilight_initial_votes = 12 # 12 votes for Twilight
    twilight_discard_divisor = 2 # half the votes for Twilight
    twilight_altered_votes = twilight_initial_votes / twilight_discard_divisor

    # L4
    got_initial_votes = 10 # 10 votes for Game of Thrones
    total_altered_votes = twilight_altered_votes + taotd_altered_votes + got_initial_votes

    # L5
    percent_multiplier = 100 # WK
    got_percentage = got_initial_votes / total_altered_votes * percent_multiplier

    # FA
    answer = got_percentage
    return answer