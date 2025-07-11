def solve():
    """Index: 2315.
    Returns: Samir's age five years from now.
    """
    # L1
    future_hania_age = 45 # Hania will be 45 years old
    future_years = 5 # in five years
    current_hania_age = future_hania_age - future_years

    # L2
    years_ago = 10 # 10 years ago
    hania_age_ten_years_ago = current_hania_age - years_ago

    # L3
    half_divisor = 2 # half the age
    samir_current_age = hania_age_ten_years_ago / half_divisor

    # L4
    samir_future_age = samir_current_age + future_years

    # FA
    answer = samir_future_age
    return answer