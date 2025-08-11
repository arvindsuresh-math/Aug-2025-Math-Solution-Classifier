def solve():
    """Index: 6988.
    Returns: the remaining safe amount of caffeine Brandy can consume.
    """
    # L1
    caffeine_per_drink = 120 # 120 mg of caffeine
    drinks_consumed = 4 # Brandy drinks 4 of them
    caffeine_drank = caffeine_per_drink * drinks_consumed

    # L2
    max_safe_caffeine = 500 # 500 mg
    remaining_safe_caffeine = max_safe_caffeine - caffeine_drank

    # FA
    answer = remaining_safe_caffeine
    return answer