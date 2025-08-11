def solve():
    """Index: 1545.
    Returns: the total amount Nina spends on presents for her children.
    """
    # L1
    num_toys = 3 # three toys
    price_per_toy = 10 # $10 each
    toys_total = num_toys * price_per_toy

    # L2
    num_card_packs = 2 # two packs of basketball cards
    price_per_card_pack = 5 # $5 each
    cards_total = num_card_packs * price_per_card_pack

    # L3
    num_shirts = 5 # five shirts
    price_per_shirt = 6 # $6 each
    shirts_total = num_shirts * price_per_shirt

    # L4
    total_spent = toys_total + cards_total + shirts_total

    # FA
    answer = total_spent
    return answer