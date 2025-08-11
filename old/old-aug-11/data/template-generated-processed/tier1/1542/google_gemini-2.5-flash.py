def solve():
    """Index: 1542.
    Returns: the total amount of nylon needed for dog and cat collars.
    """
    # L1
    nylon_per_dog_collar = 18 # 18 inches of nylon to make a dog collar
    num_dog_collars = 9 # 9 dog collars
    total_nylon_dog_collars = nylon_per_dog_collar * num_dog_collars

    # L2
    nylon_per_cat_collar = 10 # 10 inches to make a cat collar
    num_cat_collars = 3 # 3 cat collars
    total_nylon_cat_collars = nylon_per_cat_collar * num_cat_collars

    # L3
    total_nylon_needed = total_nylon_dog_collars + total_nylon_cat_collars

    # FA
    answer = total_nylon_needed
    return answer