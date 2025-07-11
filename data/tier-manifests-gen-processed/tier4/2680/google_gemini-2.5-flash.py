def solve():
    """Index: 2680.
    Returns: the total time in years to find both artifacts.
    """
    # L1
    research_months = 6 # 6 months researching
    months_per_year = 12 # WK
    research_years = research_months / months_per_year

    # L2
    expedition_years = 2 # 2-year-long expedition
    first_artifact_total_years = expedition_years + research_years

    # L3
    second_artifact_time_multiplier = 3 # 3 times as long
    second_artifact_total_years = first_artifact_total_years * second_artifact_time_multiplier

    # L4
    total_time = first_artifact_total_years + second_artifact_total_years

    # FA
    answer = total_time
    return answer