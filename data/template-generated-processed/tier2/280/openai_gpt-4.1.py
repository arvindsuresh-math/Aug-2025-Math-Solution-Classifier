def solve():
    """Index: 280.
    Returns: the total cost, in dollars, of the cards the boy bought.
    """
    # L1
    first_box_card_cost = 1.25 # cards that cost $1.25 each
    second_box_card_cost = 1.75 # cards that cost $1.75 each
    cost_per_pair = first_box_card_cost + second_box_card_cost

    # L2
    num_cards_per_box = 6 # buys 6 cards from each box
    total_cost = cost_per_pair * num_cards_per_box

    # FA
    answer = total_cost
    return answer