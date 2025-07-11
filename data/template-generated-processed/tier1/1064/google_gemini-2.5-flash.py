def solve():
    """Index: 1064.
    Returns: the total annual cost to feed all pets.
    """
    # L1
    cost_per_snake = 10 # $10 to feed each snake
    num_snakes = 4 # 4 snakes
    monthly_snake_cost = cost_per_snake * num_snakes

    # L2
    cost_per_iguana = 5 # $5 to feed each iguana
    num_iguanas = 2 # 2 iguanas
    monthly_iguana_cost = cost_per_iguana * num_iguanas

    # L3
    cost_per_gecko = 15 # $15 to feed each gecko
    num_geckos = 3 # 3 geckos
    monthly_gecko_cost = cost_per_gecko * num_geckos

    # L4
    total_monthly_cost = monthly_snake_cost + monthly_iguana_cost + monthly_gecko_cost

    # L5
    months_per_year = 12 # WK
    total_annual_cost = total_monthly_cost * months_per_year

    # FA
    answer = total_annual_cost
    return answer