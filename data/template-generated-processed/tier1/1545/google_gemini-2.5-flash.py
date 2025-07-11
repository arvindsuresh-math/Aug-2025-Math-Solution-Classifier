def solve():
    """Index: 1545.
    Returns: the total amount Nina spends.
    """
    # L1
    num_toys = 3 # three toys
    cost_per_toy = 10 # $10 each
    cost_toys = num_toys * cost_per_toy

    # L2
    num_card_packs = 2 # two packs of basketball cards
    cost_per_card_pack = 5 # $5 each
    cost_card_packs = num_card_packs * cost_per_card_pack

    # L3
    num_shirts = 5 # five shirts
    cost_per_shirt = 6 # $6 each
    cost_shirts = num_shirts * cost_per_shirt

    # L4
    total_spend = cost_toys + cost_card_packs + cost_shirts

    # FA
    answer = total_spend
    return answer