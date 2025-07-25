def solve():
    """Index: 2844.
    Returns: the total number of dolls in Lucy's collection after the addition.
    """
    # L2
    increase_dolls = 2 # Ethyl bought Lucy two new dolls
    percent_increase = 0.25 # increased the doll collection by 25%
    # L3
    original_dolls = increase_dolls / percent_increase
    # L4
    total_dolls = original_dolls + increase_dolls
    # FA
    answer = total_dolls
    return answer