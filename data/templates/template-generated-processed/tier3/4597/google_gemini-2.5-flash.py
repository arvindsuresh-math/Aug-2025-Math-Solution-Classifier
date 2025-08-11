from fractions import Fraction

def solve():
    """Index: 4597.
    Returns: the total weight of the salad dressing in grams.
    """
    # L1
    bowl_volume = 150 # bowl that holds 150 ml
    oil_proportion = Fraction(2, 3) # fills it 2/3rds with oil
    oil_volume = bowl_volume * oil_proportion

    # L2
    vinegar_proportion = Fraction(1, 3) # 1/3rd with vinegar
    vinegar_volume = bowl_volume * vinegar_proportion

    # L3
    oil_density = 5 # The oil weighs 5 g/ml
    oil_weight = oil_volume * oil_density

    # L4
    vinegar_density = 4 # the vinegar weighs 4 g/ml
    vinegar_weight = vinegar_volume * vinegar_density

    # L5
    total_dressing_weight = oil_weight + vinegar_weight

    # FA
    answer = total_dressing_weight
    return answer