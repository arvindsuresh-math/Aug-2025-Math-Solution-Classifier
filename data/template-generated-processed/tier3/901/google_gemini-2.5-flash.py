def solve():
    """Index: 901.
    Returns: the total amount Gillian spent at the farmer's market.
    """
    # L1
    sandi_initial_money = 600 # Sandi had $600
    half_divisor = 2 # spent half of it
    sandi_spent = sandi_initial_money / half_divisor

    # L2
    gillian_multiplier = 3 # three times Sandi's total
    gillian_more_spent = 150 # spent $150 more
    gillian_spent = sandi_spent * gillian_multiplier + gillian_more_spent

    # FA
    answer = gillian_spent
    return answer