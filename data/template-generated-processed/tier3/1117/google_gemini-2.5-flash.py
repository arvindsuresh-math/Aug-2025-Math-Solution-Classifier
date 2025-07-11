def solve():
    """Index: 1117.
    Returns: Lucas's age three years from now.
    """
    # L1
    gladys_age = 30 # Gladys who is 30 years old now
    billy_age_divisor = 3 # Billy is 3 times younger than Gladys
    billy_age = gladys_age / billy_age_divisor

    # L2
    sum_divisor = 2 # twice the sum of the ages of Billy and Lucas
    sum_billy_lucas_ages = gladys_age / sum_divisor

    # L3
    lucas_current_age = sum_billy_lucas_ages - billy_age

    # L4
    years_from_now = 3 # three years from now
    lucas_future_age = lucas_current_age + years_from_now

    # FA
    answer = lucas_future_age
    return answer