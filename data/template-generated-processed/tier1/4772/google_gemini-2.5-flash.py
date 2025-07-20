def solve():
    """Index: 4772.
    Returns: the total number of teeth Vann will clean today.
    """
    # L1
    dog_teeth_per_dog = 42 # Dogs have 42 teeth
    num_dogs = 5 # 5 dogs
    total_dog_teeth = dog_teeth_per_dog * num_dogs

    # L2
    cat_teeth_per_cat = 30 # cats have 30 teeth
    num_cats = 10 # 10 cats
    total_cat_teeth = cat_teeth_per_cat * num_cats

    # L3
    pig_teeth_per_pig = 28 # pigs have 28 teeth
    num_pigs = 7 # 7 pigs
    total_pig_teeth = pig_teeth_per_pig * num_pigs

    # L4
    total_teeth_cleaned = total_dog_teeth + total_cat_teeth + total_pig_teeth

    # FA
    answer = total_teeth_cleaned
    return answer