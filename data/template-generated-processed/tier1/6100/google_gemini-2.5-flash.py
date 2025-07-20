def solve():
    """Index: 6100.
    Returns: the total number of grandchildren Olga has.
    """
    # L1
    num_daughters = 3 # 3 daughters
    sons_per_daughter = 6 # each have 6 sons
    grandsons_from_daughters = num_daughters * sons_per_daughter

    # L2
    num_sons = 3 # 3 sons
    daughters_per_son = 5 # each of her sons has 5 daughters
    granddaughters_from_sons = num_sons * daughters_per_son

    # L3
    total_grandchildren = grandsons_from_daughters + granddaughters_from_sons

    # FA
    answer = total_grandchildren
    return answer