def solve():
    """Index: 2490.
    Returns: the total number of animals for sale in the pet store.
    """
    # L1
    dogs_for_sale = 6 # six dogs for sale
    cats_divisor = 2 # half as many cats
    cats_for_sale = dogs_for_sale / cats_divisor

    # L2
    birds_multiplier = 2 # twice as many birds
    birds_for_sale = dogs_for_sale * birds_multiplier

    # L3
    fish_multiplier = 3 # thrice as many fish
    fish_for_sale = dogs_for_sale * fish_multiplier

    # L4
    total_animals = dogs_for_sale + cats_for_sale + birds_for_sale + fish_for_sale

    # FA
    answer = total_animals
    return answer