def solve():
    """Index: 4891.
    Returns: the total money Khalil paid Mr. Sean.
    """
    # L1
    num_dogs = 20 # 20 dogs
    charge_per_dog = 60 # $60 to treat a dog
    cost_dogs = num_dogs * charge_per_dog

    # L2
    charge_per_cat = 40 # $40 to care for a cat
    num_cats = 60 # 60 cats
    cost_cats = charge_per_cat * num_cats

    # L3
    total_cost = cost_cats + cost_dogs

    # FA
    answer = total_cost
    return answer