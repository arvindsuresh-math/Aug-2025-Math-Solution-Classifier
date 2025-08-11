def solve():
    """Index: 189.
    Returns: Ironman's age in years.
    """
    # L1
    thor_age = 1456 # Thor is 1456 years old
    thor_to_captain_ratio = 13 # Thor is 13 times older than Captain America
    captain_america_age = thor_age / thor_to_captain_ratio

    # L2
    captain_to_peter_ratio = 7 # Captain America is 7 times older than Peter Parker
    peter_parker_age = captain_america_age / captain_to_peter_ratio

    # L3
    ironman_older_by = 32 # Ironman is 32 years older than Peter Parker
    ironman_age = peter_parker_age + ironman_older_by

    # FA
    answer = ironman_age
    return answer