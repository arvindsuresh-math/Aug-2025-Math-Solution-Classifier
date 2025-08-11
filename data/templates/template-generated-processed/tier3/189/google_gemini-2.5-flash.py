def solve():
    """Index: 189.
    Returns: Ironman's age.
    """
    # L1
    thor_age = 1456 # Thor is 1456 years old
    thor_age_multiple_of_captain_america = 13 # Thor is 13 times older than Captain America
    captain_america_age = thor_age / thor_age_multiple_of_captain_america

    # L2
    captain_america_age_multiple_of_peter_parker = 7 # Captain America is 7 times older than Peter Parker
    peter_parker_age = captain_america_age / captain_america_age_multiple_of_peter_parker

    # L3
    ironman_age_difference_from_peter_parker = 32 # Ironman is 32 years older than Peter Parker
    ironman_age = peter_parker_age + ironman_age_difference_from_peter_parker

    # FA
    answer = ironman_age
    return answer