def solve():
    """Index: 1855.
    Returns: the number of citizens in the town.
    """
    # L2
    num_cat_owners = 30 # 30 own a cat
    cat_owner_fraction = 0.5 # Half own a dog, so half own a cat
    num_pet_owners = num_cat_owners / cat_owner_fraction

    # L3
    pet_owner_percent = 0.6 # 60% of the citizens own a pet
    num_citizens = num_pet_owners / pet_owner_percent

    # FA
    answer = num_citizens
    return answer