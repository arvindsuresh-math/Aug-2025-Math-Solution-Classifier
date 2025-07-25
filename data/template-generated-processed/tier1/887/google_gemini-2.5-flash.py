def solve():
    """Index: 887.
    Returns: Kyle's age.
    """
    # L1
    tyson_age = 20 # Tyson is 20
    times_older = 2 # 2 times older than Tyson
    frederick_age = tyson_age * times_older

    # L2
    julian_younger_than_frederick = 20 # 20 years younger than Frederick
    julian_age = frederick_age - julian_younger_than_frederick

    # L3
    kyle_older_than_julian = 5 # 5 years older than Julian
    kyle_age = julian_age + kyle_older_than_julian

    # FA
    answer = kyle_age
    return answer