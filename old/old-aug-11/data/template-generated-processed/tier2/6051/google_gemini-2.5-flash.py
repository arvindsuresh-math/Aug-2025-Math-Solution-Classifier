def solve():
    """Index: 6051.
    Returns: how many kilograms more the cats weigh than the puppies.
    """
    # L1
    num_puppies = 4 # 4 puppies
    puppy_weight_kg = 7.5 # each weigh 7.5 kilograms
    total_puppy_weight = num_puppies * puppy_weight_kg

    # L2
    num_cats = 14 # 14 cats
    cat_weight_kg = 2.5 # each weigh 2.5 kilograms
    total_cat_weight = num_cats * cat_weight_kg

    # L3
    weight_difference = total_cat_weight - total_puppy_weight

    # FA
    answer = weight_difference
    return answer