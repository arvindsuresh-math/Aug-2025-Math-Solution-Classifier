def solve():
    """Index: 2714.
    Returns: the total cost to purchase all of the pets for sale at the pet shop, in dollars.
    """
    # L1
    puppy_to_parakeet_ratio = 3 # Puppies were three times more expensive than the parakeets
    parakeet_cost = 10 # the cost of one parakeet was $10
    puppy_cost = puppy_to_parakeet_ratio * parakeet_cost

    # L2
    parakeet_to_kitten_ratio = 2 # Parakeets were half as expensive as the kittens
    kitten_cost = parakeet_to_kitten_ratio * parakeet_cost

    # L3
    num_puppies = 2 # Two puppies
    total_puppy_cost = num_puppies * puppy_cost

    # L4
    num_kittens = 2 # two kittens
    total_kitten_cost = num_kittens * kitten_cost

    # L5
    num_parakeets = 3 # three parakeets
    total_parakeet_cost = num_parakeets * parakeet_cost

    # L6
    total_cost = total_puppy_cost + total_kitten_cost + total_parakeet_cost

    # FA
    answer = total_cost
    return answer