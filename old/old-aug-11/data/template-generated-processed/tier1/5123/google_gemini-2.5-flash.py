def solve():
    """Index: 5123.
    Returns: the amount of change Olivia received.
    """
    # L1
    num_basketball_packs = 2 # two packs of basketball cards
    cost_basketball_pack = 3 # $3 each
    cost_basketball_cards = num_basketball_packs * cost_basketball_pack

    # L2
    num_baseball_decks = 5 # 5 decks of baseball cards
    cost_baseball_deck = 4 # $4 each
    cost_baseball_cards = num_baseball_decks * cost_baseball_deck

    # L3
    total_cost = cost_basketball_cards + cost_baseball_cards

    # L4
    bill_amount = 50 # one $50 bill
    change_received = bill_amount - total_cost

    # FA
    answer = change_received
    return answer