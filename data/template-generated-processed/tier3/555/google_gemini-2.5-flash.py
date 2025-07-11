def solve():
    """Index: 555.
    Returns: the total number of pairs of shoes they have.
    """
    # L1
    edward_multiplier = 3 # Edward has 3 times the number of shoes Brian has
    brian_shoes = 22 # Brian has 22 pairs of shoes
    edward_shoes = edward_multiplier * brian_shoes

    # L2
    jacob_divisor = 2 # Jacob has half the number of shoes Edward has
    jacob_shoes = edward_shoes / jacob_divisor

    # L3
    total_shoes = brian_shoes + edward_shoes + jacob_shoes

    # FA
    answer = total_shoes
    return answer