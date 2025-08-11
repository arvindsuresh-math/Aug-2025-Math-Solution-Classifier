def solve():
    """Index: 1109.
    Returns: the total number of fruits the three children have.
    """
    # L2
    mike_oranges = 3 # Mike received 3 oranges
    multiplier_twice = 2 # twice as many apples
    matt_apples = mike_oranges * multiplier_twice

    # L3
    mark_bananas = matt_apples + mike_oranges

    # L4
    total_fruits = mike_oranges + matt_apples + mark_bananas

    # FA
    answer = total_fruits
    return answer