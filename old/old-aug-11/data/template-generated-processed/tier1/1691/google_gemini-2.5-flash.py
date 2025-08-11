def solve():
    """Index: 1691.
    Returns: the number of fruits remaining in Tom's fruit bowl.
    """
    # L1
    oranges = 3 # 3 oranges
    lemons = 6 # 6 lemons
    total_initial_fruits = oranges + lemons

    # L2
    fruits_eaten = 3 # eats 3 of the fruits
    remaining_fruits = total_initial_fruits - fruits_eaten

    # FA
    answer = remaining_fruits
    return answer