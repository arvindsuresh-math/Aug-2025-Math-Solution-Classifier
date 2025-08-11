def solve():
    """Index: 6632.
    Returns: the total number of red cards the team would collect.
    """
    # L1
    total_players = 11 # team of 11 players
    players_no_caution = 5 # 5 of them didn't receive cautions
    cautioned_players = total_players - players_no_caution

    # L2
    yellow_cards_per_cautioned_player = 1 # the rest received one yellow card each
    total_yellow_cards = cautioned_players * yellow_cards_per_cautioned_player

    # L3
    yellow_cards_per_red_card = 2 # each red card corresponds to 2 yellow cards
    total_red_cards = total_yellow_cards / yellow_cards_per_red_card

    # FA
    answer = total_red_cards
    return answer