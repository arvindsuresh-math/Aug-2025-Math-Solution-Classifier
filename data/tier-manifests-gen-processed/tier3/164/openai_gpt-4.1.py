def solve():
    """Index: 164.
    Returns: the number of baseball cards Buddy has on Thursday.
    """
    # L1
    monday_cards = 30 # Buddy has 30 baseball cards
    tuesday_divisor = 2 # loses half of them
    tuesday_cards = monday_cards / tuesday_divisor

    # L2
    wednesday_purchase = 12 # buys 12 baseball cards
    wednesday_cards = tuesday_cards + wednesday_purchase

    # L3
    thursday_divisor = 3 # buys a third of what he had on Tuesday
    thursday_purchase = tuesday_cards / thursday_divisor

    # L4
    thursday_cards = wednesday_cards + thursday_purchase

    # FA
    answer = thursday_cards
    return answer