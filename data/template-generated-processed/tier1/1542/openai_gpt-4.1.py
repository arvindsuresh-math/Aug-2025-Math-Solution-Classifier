def solve():
    """Index: 1542.
    Returns: the total number of inches of nylon needed for 9 dog collars and 3 cat collars.
    """
    # L1
    nylon_per_dog = 18 # 18 inches of nylon to make a dog collar
    num_dog_collars = 9 # 9 dog collars
    dog_nylon = nylon_per_dog * num_dog_collars

    # L2
    nylon_per_cat = 10 # 10 inches to make a cat collar
    num_cat_collars = 3 # 3 cat collars
    cat_nylon = nylon_per_cat * num_cat_collars

    # L3
    total_nylon = dog_nylon + cat_nylon

    # FA
    answer = total_nylon
    return answer