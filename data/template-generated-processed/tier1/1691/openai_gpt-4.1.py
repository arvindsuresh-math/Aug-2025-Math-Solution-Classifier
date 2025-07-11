def solve():
    """Index: 1691.
    Returns: the number of fruits remaining in Tom's fruit bowl after he eats 3 fruits.
    """
    # L1
    oranges = 3 # 3 oranges
    lemons = 6 # 6 lemons
    total_fruits = oranges + lemons

    # L2
    fruits_eaten = 3 # eats 3 of the fruits
    fruits_remaining = total_fruits - fruits_eaten

    # FA
    answer = fruits_remaining
    return answer