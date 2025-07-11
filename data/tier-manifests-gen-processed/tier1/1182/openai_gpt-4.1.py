def solve():
    """Index: 1182.
    Returns: the total ounces of pet food Mrs. Anderson bought.
    """
    # L1
    num_cat_bags = 2 # 2 bags of 3-pound bag of cat food
    cat_bag_weight = 3 # 3-pound bag of cat food
    total_cat_pounds = num_cat_bags * cat_bag_weight

    # L2
    dog_bag_extra = 2 # each weigh 2 more pounds than each bag of cat food
    dog_bag_weight = cat_bag_weight + dog_bag_extra

    # L3
    num_dog_bags = 2 # another 2 bags of dog food
    total_dog_pounds = num_dog_bags * dog_bag_weight

    # L4
    total_pet_pounds = total_cat_pounds + total_dog_pounds

    # L5
    ounces_per_pound = 16 # 16 ounces in each pound
    total_ounces = total_pet_pounds * ounces_per_pound

    # FA
    answer = total_ounces
    return answer