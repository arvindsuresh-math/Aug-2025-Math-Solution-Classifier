def solve():
    """Index: 1182.
    Returns: the total ounces of pet food Mrs. Anderson bought.
    """
    # L1
    num_cat_bags = 2 # 2 bags of 3-pound bag of cat food
    weight_per_cat_bag = 3 # 3-pound bag of cat food
    total_cat_food_pounds = num_cat_bags * weight_per_cat_bag

    # L2
    dog_food_extra_pounds = 2 # 2 more pounds than each bag of cat food
    weight_per_dog_bag = weight_per_cat_bag + dog_food_extra_pounds

    # L3
    num_dog_bags = 2 # another 2 bags of dog food
    total_dog_food_pounds = num_dog_bags * weight_per_dog_bag

    # L4
    total_pet_food_pounds = total_cat_food_pounds + total_dog_food_pounds

    # L5
    ounces_per_pound = 16 # 16 ounces in each pound
    total_pet_food_ounces = total_pet_food_pounds * ounces_per_pound

    # FA
    answer = total_pet_food_ounces
    return answer