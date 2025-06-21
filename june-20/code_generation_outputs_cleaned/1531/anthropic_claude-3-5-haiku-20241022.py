def solve(
    years_getting_healthy: int = 2,  # 2 years of working out to get healthy
    mountain_learning_multiplier: int = 2,  # twice as long learning mountain climbing
    months_per_mountain: int = 5,  # 5 months climbing each mountain
    num_mountains: int = 7,  # seven summits
    diving_learning_months: int = 13,  # 13 months learning to dive
    diving_years: int = 2  # 2 years diving through caves
):
    """Index: 1531.
    Returns: the total time taken to complete all bucket list goals in years."""
    #: L1
    years_learning_to_climb = years_getting_healthy * mountain_learning_multiplier

    #: L2
    months_climbing_mountains = months_per_mountain * num_mountains

    #: L3
    months_after_mountain_climbing = months_climbing_mountains + diving_learning_months

    #: L4
    years_after_mountain_climbing = months_after_mountain_climbing / 12

    #: L5
    total_years = years_getting_healthy + years_learning_to_climb + years_after_mountain_climbing + diving_years

    answer = total_years  # FINAL ANSWER
    return answer