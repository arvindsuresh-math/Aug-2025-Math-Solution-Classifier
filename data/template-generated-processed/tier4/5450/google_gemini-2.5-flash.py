def solve():
    """Index: 5450.
    Returns: the number of baby hawks expected to remain after losses.
    """
    # L1
    pregnancies_per_kettle = 15 # 15 pregnancies
    babies_per_pregnancy = 4 # 4 babies per batch
    babies_per_kettle = pregnancies_per_kettle * babies_per_pregnancy

    # L2
    num_kettles = 6 # tracking 6 kettles of hawks
    total_expected_babies = babies_per_kettle * num_kettles

    # L3
    loss_percentage_num = 25 # approximately 25% are lost
    percent_divisor = 100 # WK
    loss_proportion = loss_percentage_num / percent_divisor

    # L4
    babies_lost = total_expected_babies * loss_proportion

    # L5
    remaining_babies = total_expected_babies - babies_lost

    # FA
    answer = remaining_babies
    return answer