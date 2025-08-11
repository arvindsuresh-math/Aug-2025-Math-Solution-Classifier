def solve():
    """Index: 7038.
    Returns: the number of pets remaining at the store.
    """
    # L1
    num_puppies = 7 # 7 puppies
    num_kittens = 6 # 6 kittens
    total_initial_pets = num_puppies + num_kittens

    # L2
    puppies_sold = 2 # Two puppies
    kittens_sold = 3 # three kittens
    total_sold_pets = puppies_sold + kittens_sold

    # L3
    remaining_pets = total_initial_pets - total_sold_pets

    # FA
    answer = remaining_pets
    return answer