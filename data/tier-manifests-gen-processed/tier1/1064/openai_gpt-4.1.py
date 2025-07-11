def solve():
    """Index: 1064.
    Returns: the total amount Harry spends every year to feed all his pets.
    """
    # L1
    cost_per_snake = 10 # $10 to feed each snake
    num_snakes = 4 # 4 snakes
    snake_monthly = cost_per_snake * num_snakes

    # L2
    cost_per_iguana = 5 # $5 to feed each iguana
    num_iguanas = 2 # 2 iguanas
    iguana_monthly = cost_per_iguana * num_iguanas

    # L3
    cost_per_gecko = 15 # $15 to feed each gecko
    num_geckos = 3 # 3 geckos
    gecko_monthly = cost_per_gecko * num_geckos

    # L4
    total_monthly = snake_monthly + iguana_monthly + gecko_monthly

    # L5
    months_per_year = 12 # WK
    total_yearly = total_monthly * months_per_year

    # FA
    answer = total_yearly
    return answer