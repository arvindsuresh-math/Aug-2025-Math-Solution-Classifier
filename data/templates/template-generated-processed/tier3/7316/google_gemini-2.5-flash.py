def solve():
    """Index: 7316.
    Returns: the remaining ounces of vinegar.
    """
    # L1
    num_jars = 4 # 4 jars
    pickles_per_jar = 12 # Each jar can hold 12 pickles
    pickles_from_jars = num_jars * pickles_per_jar

    # L2
    num_cucumbers = 10 # 10 cucumbers
    pickles_per_cucumber = 6 # Each cucumber makes six pickles
    pickles_from_cucumbers = num_cucumbers * pickles_per_cucumber

    # L3
    total_vinegar_oz = 100 # 100 oz of vinegar
    vinegar_per_jar = 10 # 10 ounces of vinegar per jar
    jars_from_vinegar = total_vinegar_oz / vinegar_per_jar

    # L4
    pickles_from_vinegar = jars_from_vinegar * pickles_per_cucumber

    # L5
    # The solution implies that pickles_from_jars is the limiting factor.
    max_pickles_can_make = pickles_from_jars

    # L6
    jars_needed = max_pickles_can_make / pickles_per_jar

    # L7
    vinegar_needed = jars_needed * vinegar_per_jar

    # L8
    vinegar_remaining = total_vinegar_oz - vinegar_needed

    # FA
    answer = vinegar_remaining
    return answer