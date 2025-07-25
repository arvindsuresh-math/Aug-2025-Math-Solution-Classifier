def solve():
    """Index: 4028.
    Returns: the number of pets Lucas has enough room for.
    """
    # L1
    existing_pet_beds = 12 # 12 pet beds
    new_pet_beds = 8 # another 8 pet beds
    total_pet_beds = existing_pet_beds + new_pet_beds

    # L2
    beds_per_pet = 2 # each pet is going to need 2 beds each
    pets_room_for = total_pet_beds / beds_per_pet

    # FA
    answer = pets_room_for
    return answer