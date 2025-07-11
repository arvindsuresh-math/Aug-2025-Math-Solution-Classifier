def solve():
    """Index: 888.
    Returns: the total number of pets all three people have combined.
    """
    # L1
    teddy_dogs = 7 # Teddy has 7 dogs
    teddy_cats = 8 # Teddy has 8 cats
    teddy_pets = teddy_dogs + teddy_cats

    # L2
    ben_more_dogs = 9 # Ben has 9 more dogs than Teddy
    ben_dogs = ben_more_dogs + teddy_dogs
    ben_pets = ben_dogs # Ben has only dogs, so pets = dogs

    # L3
    dave_more_cats = 13 # Dave has 13 more cats than Teddy
    dave_cats = dave_more_cats + teddy_cats

    # L4
    dave_less_dogs = 5 # Dave has 5 less dogs than Teddy
    dave_dogs = teddy_dogs - dave_less_dogs

    # L5
    dave_pets = dave_cats + dave_dogs

    # L6
    total_pets = teddy_pets + ben_pets + dave_pets

    # FA
    answer = total_pets
    return answer