def solve():
    """Index: 862.
    Returns: the number of additional acorns each squirrel needs to collect.
    """
    # L1
    total_acorns = 575 # 575 acorns
    num_squirrels = 5 # 5 squirrels
    acorns_per_squirrel = total_acorns / num_squirrels

    # L2
    acorns_needed_per_squirrel = 130 # each squirrel needs 130 acorns
    acorns_still_needed_per_squirrel = acorns_needed_per_squirrel - acorns_per_squirrel

    # FA
    answer = acorns_still_needed_per_squirrel
    return answer