from fractions import Fraction

def solve():
    """Index: 969.
    Returns: the total number of frogs in the two lakes.
    """
    # L1
    fewer_percentage = Fraction(20, 100) # twenty percent fewer frogs
    lassie_lake_frogs = 45 # forty-five frogs
    fewer_frogs_crystal = fewer_percentage * lassie_lake_frogs

    # L2
    crystal_lake_frogs = lassie_lake_frogs - fewer_frogs_crystal

    # L3
    total_frogs = crystal_lake_frogs + lassie_lake_frogs

    # FA
    answer = total_frogs
    return answer