def solve():
    """Index: 7159.
    Returns: the average weight of the three individuals.
    """
    # L1
    jalen_weight = 160 # Jalen weighed 160 pounds
    ponce_lighter_than_jalen = 10 # Ponce was 10 pounds lighter than Jalen
    ponce_weight = jalen_weight - ponce_lighter_than_jalen

    # L2
    jalen_ponce_sum_weight = ponce_weight + jalen_weight

    # L3
    ishmael_heavier_than_ponce = 20 # Ishmael was 20 pounds heavier than Ponce
    ishmael_weight = ponce_weight + ishmael_heavier_than_ponce

    # L4
    total_weight = jalen_ponce_sum_weight + ishmael_weight

    # L5
    number_of_people = 3 # WK
    average_weight = total_weight / number_of_people

    # FA
    answer = average_weight
    return answer