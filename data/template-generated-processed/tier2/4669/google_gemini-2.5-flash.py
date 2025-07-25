def solve():
    """Index: 4669.
    Returns: the total cost of the deck.
    """
    # L1
    num_rare_cards = 19 # 19 rare cards
    cost_rare_card = 1 # rare cards cost $1
    cost_rares = num_rare_cards * cost_rare_card

    # L2
    num_uncommon_cards = 11 # 11 uncommon
    cost_uncommon_card = 0.5 # uncommon are $.50
    cost_uncommons = num_uncommon_cards * cost_uncommon_card

    # L3
    num_common_cards = 30 # 30 commons
    cost_common_card = 0.25 # commons are $.25 each
    cost_commons = num_common_cards * cost_common_card

    # L4
    total_cost = cost_rares + cost_uncommons + cost_commons

    # FA
    answer = total_cost
    return answer