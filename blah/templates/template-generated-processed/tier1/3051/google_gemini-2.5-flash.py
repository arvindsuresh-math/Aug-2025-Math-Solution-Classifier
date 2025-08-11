def solve():
    """Index: 3051.
    Returns: the total cost to get the animals ready for adoption.
    """
    # L1
    num_cats = 2 # 2 cats
    cost_per_cat = 50 # 50 dollars to get cats ready for adoption
    cost_cats = num_cats * cost_per_cat

    # L2
    num_adult_dogs = 3 # 3 adult dogs
    cost_per_adult_dog = 100 # 100 dollars to get adult dogs ready for adoption
    cost_adult_dogs = num_adult_dogs * cost_per_adult_dog

    # L3
    num_puppies = 2 # 2 puppies
    cost_per_puppy = 150 # 150 to get puppies ready for adoption
    cost_puppies = num_puppies * cost_per_puppy

    # L4
    total_cost = cost_adult_dogs + cost_puppies + cost_cats

    # FA
    answer = total_cost
    return answer