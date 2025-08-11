def solve():
    """Index: 2090.
    Returns: the combined weight of the bags after removing 4 kg.
    """
    # L1
    sugar_weight = 16 # A bag full of sugar weighs 16 kg
    salt_weight = 30 # A bag full of salt weighs 30 kg
    combined_weight = sugar_weight + salt_weight

    # L2
    removed_weight = 4 # remove 4 kg
    new_weight = combined_weight - removed_weight

    # FA
    answer = new_weight
    return answer