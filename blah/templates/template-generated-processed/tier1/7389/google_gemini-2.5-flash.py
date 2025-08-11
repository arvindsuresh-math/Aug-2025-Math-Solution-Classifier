def solve():
    """Index: 7389.
    Returns: Teresa's age when she gave birth to Michiko.
    """
    # L1
    morio_current_age = 71 # her husband Morio is 71 years old
    teresa_current_age = 59 # Teresa is 59
    age_difference = morio_current_age - teresa_current_age

    # L2
    morio_age_at_birth = 38 # Michiko was born when Morio was 38
    teresa_age_at_birth = morio_age_at_birth - age_difference

    # FA
    answer = teresa_age_at_birth
    return answer