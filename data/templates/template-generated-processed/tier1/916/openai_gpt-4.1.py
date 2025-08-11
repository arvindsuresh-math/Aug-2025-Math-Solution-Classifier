def solve():
    """Index: 916.
    Returns: the total number of pencils Asaf and Alexander have together.
    """
    # L1
    sum_ages = 140 # the sum of their ages is 140
    asaf_age = 50 # Asaf is 50 years old
    alexander_age = sum_ages - asaf_age

    # L2
    age_difference = alexander_age - asaf_age

    # L3
    multiplier_for_half = 2 # half the total number of pencils Asaf has
    asaf_pencils = multiplier_for_half * age_difference

    # L4
    alexander_more_pencils = 60 # Alexander has 60 more pencils than Asaf
    alexander_pencils = asaf_pencils + alexander_more_pencils

    # L5
    total_pencils = alexander_pencils + asaf_pencils

    # FA
    answer = total_pencils
    return answer