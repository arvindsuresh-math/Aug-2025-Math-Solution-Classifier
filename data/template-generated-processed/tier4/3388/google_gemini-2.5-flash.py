def solve():
    """Index: 3388.
    Returns: the total weight of Jacque's suitcase on the return flight home in pounds.
    """
    # L1
    num_perfume_bottles = 5 # 5 bottles of perfume
    perfume_weight_per_bottle = 1.2 # 1.2 ounces each
    total_perfume_weight_oz = num_perfume_bottles * perfume_weight_per_bottle

    # L2
    num_soap_bars = 2 # 2 bars of soap
    soap_weight_per_bar = 5 # 5 ounces each
    total_soap_weight_oz = num_soap_bars * soap_weight_per_bar

    # L3
    num_jam_jars = 2 # 2 jars of jam
    jam_weight_per_jar = 8 # 8 ounces each
    total_jam_weight_oz = num_jam_jars * jam_weight_per_jar

    # L4
    total_products_weight_oz = total_perfume_weight_oz + total_soap_weight_oz + total_jam_weight_oz

    # L5
    ounces_per_pound = 16 # Considering 16 ounces is the same as 1 pound
    total_products_weight_lbs = total_products_weight_oz / ounces_per_pound

    # L6
    initial_suitcase_weight_lbs = 5 # suitcase weighed 5 pounds
    chocolate_weight_lbs = 4 # 4 pounds of chocolate
    final_suitcase_weight_lbs = initial_suitcase_weight_lbs + chocolate_weight_lbs + total_products_weight_lbs

    # FA
    answer = final_suitcase_weight_lbs
    return answer