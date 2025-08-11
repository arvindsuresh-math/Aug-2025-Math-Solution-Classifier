def solve():
    """Index: 6661.
    Returns: the total number of pairs of shoes Helga tried on.
    """
    # L1
    shoes_store1 = 7 # tried on 7 pairs of shoes
    more_than_store1 = 2 # tried on 2 more pairs
    shoes_store2 = shoes_store1 + more_than_store1

    # L2
    shoes_store3 = 0 # did not try on any shoes
    shoes_first_three_stores = shoes_store1 + shoes_store2 + shoes_store3

    # L3
    multiplier_twice = 2 # twice as many pairs of shoes
    shoes_store4 = shoes_first_three_stores * multiplier_twice

    # L4
    total_shoes_tried_on = shoes_first_three_stores + shoes_store4

    # FA
    answer = total_shoes_tried_on
    return answer