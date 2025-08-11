def solve():
    """Index: 5234.
    Returns: the age difference between Milena and her grandfather.
    """
    # L1
    milena_age = 7 # Milena is 7 years old
    grandmother_age_multiplier = 9 # grandmother is 9 times older than her
    grandmother_age = milena_age * grandmother_age_multiplier

    # L2
    grandfather_age_difference = 2 # grandfather is two years older than her grandmother
    grandfather_age = grandmother_age + grandfather_age_difference

    # L3
    age_difference = grandfather_age - milena_age

    # FA
    answer = age_difference
    return answer