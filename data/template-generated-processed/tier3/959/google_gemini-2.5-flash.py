def solve():
    """Index: 959.
    Returns: the percentage of snowballs Janet made.
    """
    # L1
    janet_snowballs = 50 # Janet makes 50 snowballs
    brother_snowballs = 150 # her brother makes 150 snowballs
    total_snowballs = janet_snowballs + brother_snowballs

    # L2
    percentage_multiplier = 100 # multiply by 100%
    janet_percentage = (janet_snowballs / total_snowballs) * percentage_multiplier

    # FA
    answer = janet_percentage
    return answer