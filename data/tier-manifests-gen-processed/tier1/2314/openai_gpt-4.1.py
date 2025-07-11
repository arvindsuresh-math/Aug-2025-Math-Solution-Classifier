def solve():
    """Index: 2314.
    Returns: Sam's weight in pounds.
    """
    # L1
    peter_weight = 65 # Peter weighs 65 pounds
    tyler_to_peter_ratio = 2 # Peter weighs half as much as Tyler
    tyler_weight = peter_weight * tyler_to_peter_ratio

    # L2
    tyler_sam_difference = 25 # Tyler weighs 25 pounds more than Sam
    sam_weight = tyler_weight - tyler_sam_difference

    # FA
    answer = sam_weight
    return answer