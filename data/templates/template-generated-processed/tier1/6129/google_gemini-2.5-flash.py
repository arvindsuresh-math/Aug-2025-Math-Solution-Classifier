def solve():
    """Index: 6129.
    Returns: the number of more pairs of shoes Anthony has compared to Jim.
    """
    # L1
    scott_shoes = 7 # 7 pairs of shoes
    anthony_multiplier = 3 # 3 times as many pairs of shoes as Scott
    anthony_shoes = scott_shoes * anthony_multiplier

    # L2
    jim_less_than_anthony = 2 # 2 less pairs than Anthony
    jim_shoes = anthony_shoes - jim_less_than_anthony

    # L3
    difference_anthony_jim = anthony_shoes - jim_shoes

    # FA
    answer = difference_anthony_jim
    return answer