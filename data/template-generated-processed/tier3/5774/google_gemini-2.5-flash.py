def solve():
    """Index: 5774.
    Returns: the total dollars the vet donated.
    """
    # L1
    num_dogs_adopted = 8 # Eight families adopt dogs
    dog_vet_fee = 15 # Vet fees for dogs are $15
    dog_fees = num_dogs_adopted * dog_vet_fee

    # L2
    num_cats_adopted = 3 # three adopt cats
    cat_vet_fee = 13 # vet fees for cats are $13
    cat_fees = num_cats_adopted * cat_vet_fee

    # L3
    total_vet_fees = dog_fees + cat_fees

    # L4
    donation_divisor = 3 # a third of the fees
    vet_donation = total_vet_fees / donation_divisor

    # FA
    answer = vet_donation
    return answer