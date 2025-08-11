def solve():
    """Index: 3910.
    Returns: the age of Mason's father.
    """
    # L1
    mason_age = 20 # Mason is 20 years old
    sydney_age_multiplier = 3 # three times younger than Sydney
    sydney_age = mason_age * sydney_age_multiplier

    # L2
    father_age_difference = 6 # six years younger than Mason's father
    father_age = sydney_age + father_age_difference

    # FA
    answer = father_age
    return answer