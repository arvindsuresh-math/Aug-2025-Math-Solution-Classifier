def solve():
    """Index: 5109.
    Returns: the total mask production of July.
    """
    # L1
    march_production = 3000 # 3000 masks in March
    doubling_factor = 2 # doubled every month
    april_production = march_production * doubling_factor

    # L2
    may_production = doubling_factor * april_production

    # L3
    june_production = doubling_factor * may_production

    # L4
    july_production = doubling_factor * june_production

    # FA
    answer = july_production
    return answer