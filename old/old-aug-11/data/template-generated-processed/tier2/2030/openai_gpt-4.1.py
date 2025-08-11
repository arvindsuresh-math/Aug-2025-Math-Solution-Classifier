def solve():
    """Index: 2030.
    Returns: the total number of fruits that the fruit vendor sold.
    """
    # L1
    lemons_dozen = 2.5 # 2.5 dozen lemons
    dozen = 12 # WK: 1 dozen is equal to 12
    lemons_count = lemons_dozen * dozen

    # L2
    avocados_dozen = 5 # 5 dozens avocados
    avocados_count = avocados_dozen * dozen

    # L3
    total_fruits = lemons_count + avocados_count

    # FA
    answer = total_fruits
    return answer