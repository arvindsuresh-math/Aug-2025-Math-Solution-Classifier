def solve():
    """Index: 2030.
    Returns: the total number of fruits sold by the fruit vendor.
    """
    # L1
    lemons_dozens = 2.5 # 2.5 dozen lemons
    items_per_dozen = 12 # WK
    lemons_count = lemons_dozens * items_per_dozen

    # L2
    avocados_dozens = 5 # 5 dozens avocados
    avocados_count = avocados_dozens * items_per_dozen

    # L3
    total_fruits = lemons_count + avocados_count

    # FA
    answer = total_fruits
    return answer