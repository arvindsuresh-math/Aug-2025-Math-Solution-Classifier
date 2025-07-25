def solve():
    """Index: 5872.
    Returns: the total miles Jim travels.
    """
    # L1
    john_distance = 15 # John travels 15 miles on a bike ride
    jill_less_distance = 5 # Jill travels 5 miles less
    jill_distance = john_distance - jill_less_distance

    # L2
    jim_percentage_decimal = 0.20 # 20% as far as Jill
    jim_distance = jill_distance * jim_percentage_decimal

    # FA
    answer = jim_distance
    return answer