def solve():
    """Index: 1141.
    Returns: the total number of animals the pet store owner has left.
    """
    # L1
    initial_birds = 12 # 12 birds
    birds_sold_divisor = 2 # Half the birds were sold
    birds_left = initial_birds / birds_sold_divisor

    # L2
    initial_puppies = 9 # 9 puppies
    puppies_adopted = 3 # 3 puppies were adopted
    puppies_left = initial_puppies - puppies_adopted

    # L3
    initial_spiders = 15 # 15 spiders
    spiders_went_loose = 7 # 7 of them went loose
    spiders_left = initial_spiders - spiders_went_loose

    # L4
    initial_cats = 5 # 5 cats
    total_animals_left = initial_cats + birds_left + puppies_left + spiders_left

    # FA
    answer = total_animals_left
    return answer