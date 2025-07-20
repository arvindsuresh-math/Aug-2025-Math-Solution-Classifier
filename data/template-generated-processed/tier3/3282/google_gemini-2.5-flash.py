def solve():
    """Index: 3282.
    Returns: Janice's age.
    """
    # L1
    current_year = 2021 # It’s February 2021
    mark_birth_year = 1976 # Mark was born in January 1976
    mark_age = current_year - mark_birth_year

    # L2
    graham_age_difference = 3 # Graham is 3 years younger than Mark
    graham_age = mark_age - graham_age_difference

    # L3
    janice_age_divisor = 2 # 1/2 the age of Graham
    janice_age = graham_age / janice_age_divisor

    # FA
    answer = janice_age
    return answer