def solve():
    """Index: 2764.
    Returns: the number of male animals in the barn.
    """
    # L1
    horses = 100 # 100 horses
    sheep = 29 # 29 sheep
    chickens = 9 # 9 chickens
    initial_animals = horses + sheep + chickens

    # L2
    half_divisor = 2 # half of the animals
    animals_after_brian = initial_animals / half_divisor

    # L3
    goats_gifted = 37 # an additional 37 goats
    total_animals_after_gift = animals_after_brian + goats_gifted

    # L4
    male_ratio_divisor = 2 # exactly half of the animals in the barn are male animals
    male_animals = total_animals_after_gift / male_ratio_divisor

    # FA
    answer = male_animals
    return answer