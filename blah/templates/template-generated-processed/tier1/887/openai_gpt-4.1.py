def solve():
    """Index: 887.
    Returns: Kyle's age.
    """
    # L1
    tyson_age = 20 # Tyson is 20
    frederick_multiplier = 2 # Frederick is 2 times older than Tyson
    frederick_age = tyson_age * frederick_multiplier

    # L2
    julian_younger_than_frederick = 20 # Julian is 20 years younger than Frederick
    julian_age = frederick_age - julian_younger_than_frederick

    # L3
    kyle_older_than_julian = 5 # Kyle is 5 years older than Julian
    kyle_age = julian_age + kyle_older_than_julian

    # FA
    answer = kyle_age
    return answer