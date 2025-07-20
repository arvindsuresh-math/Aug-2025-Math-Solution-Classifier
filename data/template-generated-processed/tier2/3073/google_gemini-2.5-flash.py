def solve():
    """Index: 3073.
    Returns: the number of items included in each charge.
    """
    # L1
    dog_treats = 8 # 8 dog treats
    chew_toys = 2 # 2 chew toys
    initial_dog_supplies = dog_treats + chew_toys

    # L2
    rawhide_bones = 10 # 10 more rawhide bones
    total_dog_supplies = initial_dog_supplies + rawhide_bones

    # L3
    num_credit_cards = 4 # 4 credit cards
    fraction_per_card = 0.25 # WK
    items_per_charge = total_dog_supplies * fraction_per_card

    # FA
    answer = items_per_charge
    return answer