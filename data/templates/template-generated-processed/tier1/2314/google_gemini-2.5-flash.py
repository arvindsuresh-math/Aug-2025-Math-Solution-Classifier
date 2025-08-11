def solve():
    """Index: 2314.
    Returns: Sam's weight in pounds.
    """
    # L1
    peter_weight = 65 # If Peter weighs 65 pounds
    half_multiplier = 2 # Peter weighs half as much as Tyler
    tyler_weight = peter_weight * half_multiplier

    # L2
    tyler_more_than_sam = 25 # Tyler weighs 25 pounds more than Sam
    sam_weight = tyler_weight - tyler_more_than_sam

    # FA
    answer = sam_weight
    return answer