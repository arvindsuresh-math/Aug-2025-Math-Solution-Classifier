def solve():
    """Index: 280.
    Returns: the total cost of the cards bought.
    """
    # L1
    cost_card_box1 = 1.25 # cards that cost $1.25 each
    cost_card_box2 = 1.75 # cards that cost $1.75 each
    cost_one_card_from_each_box = cost_card_box1 + cost_card_box2

    # L2
    num_cards_per_box = 6 # buys 6 cards from each box
    total_cost = cost_one_card_from_each_box * num_cards_per_box

    # FA
    answer = total_cost
    return answer