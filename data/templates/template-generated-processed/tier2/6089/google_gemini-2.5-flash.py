def solve():
    """Index: 6089.
    Returns: the total amount of ounces eaten by the winner.
    """
    # L1
    javier_meat_ravioli_count = 5 # Javier eats 5 meat ravioli
    meat_ravioli_weight = 1.5 # The meat ravioli weighs 1.5 ounces each
    javier_meat_ravioli_total_weight = javier_meat_ravioli_count * meat_ravioli_weight

    # L2
    javier_pumpkin_ravioli_count = 2 # 2 pumpkin ravioli
    pumpkin_ravioli_weight = 1.25 # The pumpkin ravioli is 1.25 ounces each
    javier_pumpkin_ravioli_total_weight = javier_pumpkin_ravioli_count * pumpkin_ravioli_weight

    # L3
    javier_cheese_ravioli_count = 4 # 4 cheese ravioli
    cheese_ravioli_weight = 1 # The cheese ravioli is one ounce
    javier_cheese_ravioli_total_weight = javier_cheese_ravioli_count * cheese_ravioli_weight

    # L4
    javier_total_weight = javier_meat_ravioli_total_weight + javier_pumpkin_ravioli_total_weight + javier_cheese_ravioli_total_weight

    # L5
    brother_pumpkin_ravioli_count = 12 # had 12 of them
    brother_total_weight = brother_pumpkin_ravioli_count * pumpkin_ravioli_weight

    # L6
    winner_total_weight = brother_total_weight

    # FA
    answer = winner_total_weight
    return answer