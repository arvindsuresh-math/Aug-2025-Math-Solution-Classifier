def solve():
    """Index: 5143.
    Returns: my age when Billy was born.
    """
    # L1
    my_age_multiplier = 4 # 4 times older
    billy_current_age = 4 # Billy is 4 years old
    my_current_age = my_age_multiplier * billy_current_age

    # L2
    my_age_at_billys_birth = my_current_age - billy_current_age

    # FA
    answer = my_age_at_billys_birth
    return answer