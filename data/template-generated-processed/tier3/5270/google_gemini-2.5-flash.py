def solve():
    """Index: 5270.
    Returns: the total number of cups of pesto Cheryl can make.
    """
    # L1
    basil_per_week = 16 # 16 cups of basil from her farm every week
    number_of_weeks = 8 # for 8 weeks
    total_basil_harvested = basil_per_week * number_of_weeks

    # L2
    basil_needed_per_pesto_cup = 4 # 4 cups of basil to make 1 cup of pesto
    total_pesto_cups = total_basil_harvested / basil_needed_per_pesto_cup

    # FA
    answer = total_pesto_cups
    return answer