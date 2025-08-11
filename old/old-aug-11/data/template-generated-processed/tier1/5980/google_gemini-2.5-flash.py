def solve():
    """Index: 5980.
    Returns: the total cost of the shots.
    """
    # L1
    num_pregnant_dogs = 3 # 3 pregnant dogs
    puppies_per_dog = 4 # give birth to 4 puppies
    total_puppies = num_pregnant_dogs * puppies_per_dog

    # L2
    shots_per_puppy = 2 # Each puppy needs 2 shots
    total_shots = total_puppies * shots_per_puppy

    # L3
    cost_per_shot = 5 # each shot costs $5
    total_cost = total_shots * cost_per_shot

    # FA
    answer = total_cost
    return answer