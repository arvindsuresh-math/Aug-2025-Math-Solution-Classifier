def solve():
    """Index: 5719.
    Returns: the number of skirts Purple Valley has.
    """
    # L1
    seafoam_numerator = 2 # two-thirds as many skirts
    azure_valley_skirts = 60 # Azure Valley has 60 skirts
    seafoam_denominator = 3 # two-thirds as many skirts
    intermediate_product_l1 = seafoam_numerator * azure_valley_skirts
    seafoam_valley_skirts = intermediate_product_l1 / seafoam_denominator

    # L2
    purple_numerator = 1 # one-quarter as many skirts
    purple_denominator = 4 # one-quarter as many skirts
    purple_valley_skirts = seafoam_valley_skirts / purple_denominator

    # FA
    answer = purple_valley_skirts
    return answer