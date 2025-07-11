from fractions import Fraction

def solve():
    """Index: 2070.
    Returns: the amount Bob was refunded for the expired product.
    """
    # L1
    expired_percentage = Fraction(40, 100) # 40% of the packs were expired
    total_packs = 80 # 80 packs of Greek yogurt
    expired_packs = expired_percentage * total_packs

    # L2
    cost_per_pack = 12 # each pack was $12
    refund_amount = cost_per_pack * expired_packs

    # FA
    answer = refund_amount
    return answer