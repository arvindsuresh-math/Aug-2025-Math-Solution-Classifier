def solve():
    """Index: 513.
    Returns: the number of fruits Jennifer has left.
    """
    # L1
    multiplier_for_apples = 2 # twice as many apples
    pears = 10 # ten pears
    apples = multiplier_for_apples * pears

    # L2
    oranges = 20 # 20 oranges
    total_fruits_initial = pears + oranges + apples

    # L3
    given_per_fruit_type = 2 # two of each fruit
    fruits_given_to_sister = given_per_fruit_type + given_per_fruit_type + given_per_fruit_type

    # L4
    fruits_left = total_fruits_initial - fruits_given_to_sister

    # FA
    answer = fruits_left
    return answer