def solve():
    """Index: 941.
    Returns: the total amount of money Jean gives away to grandchildren a year.
    """
    # L1
    cards_per_grandkid = 2 # 2 cards a year
    money_per_card = 80 # $80 in each card
    money_per_grandchild_per_year = cards_per_grandkid * money_per_card

    # L2
    num_grandchildren = 3 # 3 grandchildren
    total_money_given_per_year = num_grandchildren * money_per_grandchild_per_year

    # FA
    answer = total_money_given_per_year
    return answer