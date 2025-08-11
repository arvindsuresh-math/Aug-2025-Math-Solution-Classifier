def solve():
    """Index: 164.
    Returns: the total number of baseball cards Buddy has on Thursday.
    """
    # L1
    initial_cards = 30 # On Monday Buddy has 30 baseball cards
    lost_fraction_denominator = 2 # loses half of them
    cards_on_tuesday = initial_cards / lost_fraction_denominator

    # L2
    bought_wednesday = 12 # On Wednesday Buddy buys 12 baseball cards
    cards_on_wednesday = cards_on_tuesday + bought_wednesday

    # L3
    bought_thursday_divisor = 3 # a third of what he had on Tuesday
    bought_thursday = cards_on_tuesday / bought_thursday_divisor

    # L4
    total_cards_on_thursday = cards_on_wednesday + bought_thursday

    # FA
    answer = total_cards_on_thursday
    return answer