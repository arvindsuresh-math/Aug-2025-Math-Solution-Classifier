def solve():
    """Index: 2197.
    Returns: the total number of times Missy yells at both dogs combined.
    """
    # L1
    stubborn_multiplier = 4 # four times for every one time
    obedient_yells = 12 # yells at the obedient dog 12 times
    stubborn_yells = stubborn_multiplier * obedient_yells

    # L2
    total_yells = stubborn_yells + obedient_yells

    # FA
    answer = total_yells
    return answer