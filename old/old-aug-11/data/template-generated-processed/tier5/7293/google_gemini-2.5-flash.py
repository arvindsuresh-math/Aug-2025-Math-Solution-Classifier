def solve():
    """Index: 7293.
    Returns: the number of cats Brenda needs to spay.
    """
    # L3
    total_animals = 21 # 21 animals total today
    dogs_multiplier = 2 # twice as many dogs
    combined_coefficient = 1 + dogs_multiplier

    # L4
    cats = total_animals / combined_coefficient

    # FA
    answer = cats
    return answer