def solve():
    """Index: 1910.
    Returns: the total amount of corn Johnson and his neighbor can harvest together after six months.
    """
    # L1
    johnson_yield_per_hectare = 80 # can yield 80 corn every two months
    neighbor_yield_multiplier = 2 # each hectare can yield twice the amount as Johnson
    neighbor_yield_per_hectare = johnson_yield_per_hectare * neighbor_yield_multiplier

    # L2
    neighbor_hectares = 2 # two-hectare cornfield
    neighbor_total_yield = neighbor_yield_per_hectare * neighbor_hectares

    # L3
    total_yield_per_2_months = johnson_yield_per_hectare + neighbor_total_yield

    # L4
    num_2_month_periods = 3 # 6 months / 2 months per period
    total_yield_6_months = total_yield_per_2_months * num_2_month_periods

    # FA
    answer = total_yield_6_months
    return answer