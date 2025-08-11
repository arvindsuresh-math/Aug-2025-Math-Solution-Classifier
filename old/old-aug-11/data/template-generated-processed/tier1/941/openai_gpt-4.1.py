def solve():
    """Index: 941.
    Returns: the total amount Jean gives to her grandchildren in a year.
    """
    # L1
    cards_per_grandchild = 2 # buys each grandkid 2 cards a year
    money_per_card = 80 # puts $80 in each card
    per_grandchild_per_year = cards_per_grandchild * money_per_card

    # L2
    num_grandchildren = 3 # Jean has 3 grandchildren
    total_per_year = num_grandchildren * per_grandchild_per_year

    # FA
    answer = total_per_year
    return answer