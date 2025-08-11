def solve():
    """Index: 4304.
    Returns: the age of Rachel's father when she is 25 years old.
    """
    # L1
    rachel_age = 12 # Rachel is 12 years old
    grandfather_age_multiplier = 7 # grandfather is 7 times her age
    grandfather_age = rachel_age * grandfather_age_multiplier

    # L2
    mother_age_divisor = 2 # mother is half grandfather's age
    mother_age = grandfather_age / mother_age_divisor

    # L3
    father_age_difference = 5 # father is 5 years older than her mother
    father_age = mother_age + father_age_difference

    # L4
    rachel_future_age = 25 # when she is 25 years old
    years_until_rachel_25 = rachel_future_age - rachel_age

    # L5
    father_future_age = father_age + years_until_rachel_25

    # FA
    answer = father_future_age
    return answer