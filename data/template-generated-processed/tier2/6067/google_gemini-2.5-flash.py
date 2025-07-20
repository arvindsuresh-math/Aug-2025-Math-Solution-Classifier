def solve():
    """Index: 6067.
    Returns: the number of bunnies Michael has.
    """
    # L1
    total_percent = 100 # WK
    cats_percent = 50 # 50% are cats
    dogs_percent = 25 # 25% of them are dogs
    bunnies_percent = total_percent - cats_percent - dogs_percent

    # L2
    total_pets = 36 # Michael has 36 pets
    bunnies_decimal_percent = bunnies_percent / 100
    num_bunnies = total_pets * bunnies_decimal_percent

    # FA
    answer = num_bunnies
    return answer