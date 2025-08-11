def solve():
    """Index: 4050.
    Returns: the number of fish Patrick caught.
    """
    # L1
    ollie_caught = 5 # If Ollie caught 5 fish
    angus_more_than_ollie = 7 # Ollie caught 7 fewer fish than Angus
    angus_caught = ollie_caught + angus_more_than_ollie

    # L2
    angus_more_than_patrick = 4 # Angus caught 4 more fish than Patrick did
    patrick_caught = angus_caught - angus_more_than_patrick

    # FA
    answer = patrick_caught
    return answer