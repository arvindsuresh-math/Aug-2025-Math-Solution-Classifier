def solve():
    """Index: 4113.
    Returns: the amount of money Nicholas paid more than Kenneth for the fabric.
    """
    # L1
    kenneth_fabric_oz = 700 # bought 700oz
    price_per_oz = 40 # paid $40 for an oz of fabric
    kenneth_total_spent = kenneth_fabric_oz * price_per_oz

    # L2
    nicholas_multiplier = 6 # six times as much fabric
    nicholas_fabric_oz = nicholas_multiplier * kenneth_fabric_oz

    # L3
    nicholas_total_spent = nicholas_fabric_oz * price_per_oz

    # L4
    difference_in_payment = nicholas_total_spent - kenneth_total_spent

    # FA
    answer = difference_in_payment
    return answer