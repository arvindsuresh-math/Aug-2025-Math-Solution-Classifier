def solve():
    """Index: 6796.
    Returns: the number of bottles of milk left on the store shelf.
    """
    # L1
    jason_bought = 5 # Jason buys 5 of the bottles
    harry_bought = 6 # Harry buys 6 more
    total_purchased = jason_bought + harry_bought

    # L2
    initial_bottles = 35 # 35 bottles of milk
    bottles_left = initial_bottles - total_purchased

    # FA
    answer = bottles_left
    return answer