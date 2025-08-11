def solve():
    """Index: 622.
    Returns: the total weight Anne is carrying in kilograms.
    """
    # L1
    female_cat_weight = 2 # Anne's female cat weighs 2 kilograms
    multiplier_male_cat = 2 # two times heavier
    male_cat_weight = female_cat_weight * multiplier_male_cat

    # L2
    total_weight = female_cat_weight + male_cat_weight

    # FA
    answer = total_weight
    return answer