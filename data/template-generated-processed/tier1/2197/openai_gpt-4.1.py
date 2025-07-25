def solve():
    """Index: 2197.
    Returns: the total number of times Missy yells at both dogs combined.
    """
    # L1
    stubborn_per_obedient = 4 # four times for every one time
    obedient_yells = 12 # yells at the obedient dog 12 times
    stubborn_yells = stubborn_per_obedient * obedient_yells

    # L2
    total_yells = stubborn_yells + obedient_yells

    # FA
    answer = total_yells
    return answer