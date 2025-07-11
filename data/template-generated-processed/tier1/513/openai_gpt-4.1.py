def solve():
    """Index: 513.
    Returns: the number of fruits Jennifer has left after giving her sister 2 of each fruit.
    """
    # L1
    pears = 10 # ten pears
    apples_multiplier = 2 # twice as many apples as pears
    apples = apples_multiplier * pears

    # L2
    oranges = 20 # 20 oranges
    total_fruits = pears + oranges + apples

    # L3
    pears_given = 2 # gives her sister two of each fruit
    oranges_given = 2 # gives her sister two of each fruit
    apples_given = 2 # gives her sister two of each fruit
    total_given = pears_given + oranges_given + apples_given

    # L4
    fruits_left = total_fruits - total_given

    # FA
    answer = fruits_left
    return answer