def solve():
    """Index: 5586.
    Returns: the number of freshmen and sophomores who do not own a pet.
    """
    # L1
    total_students = 400 # 400 students in a local high school
    fresh_soph_percent = 0.50 # 50 percent are freshmen or sophomores
    num_fresh_soph = total_students * fresh_soph_percent

    # L2
    pet_owner_fraction_denominator = 5 # 1/5 of freshmen and sophomores own a pet
    num_fresh_soph_with_pets = num_fresh_soph / pet_owner_fraction_denominator

    # L3
    num_fresh_soph_no_pets = num_fresh_soph - num_fresh_soph_with_pets

    # FA
    answer = num_fresh_soph_no_pets
    return answer