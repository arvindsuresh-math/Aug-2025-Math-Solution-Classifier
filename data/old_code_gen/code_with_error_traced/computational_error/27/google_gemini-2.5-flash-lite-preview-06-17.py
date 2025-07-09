def solve(
    initial_files_downloaded: int = 800, # After downloading 800 files
    percentage_deleted_first_round: float = 0.7, # he deleted 70% of them
    additional_files_downloaded: int = 400, # He downloaded 400 more files
    fraction_deleted_second_round: float = 3/5 # 3/5 of them were irrelevant
):
    """Index: 27.
    Returns: the number of valuable files Brennan was left with after deleting the unrelated files he downloaded in the second round.
    """

    #: L1
    non_valuable_files_first_round = initial_files_downloaded * percentage_deleted_first_round # eval: 560.0 = 800 * 0.7

    #: L2
    valuable_files_first_round = initial_files_downloaded - non_valuable_files_first_round # eval: 240.0 = 800 - 560.0

    #: L3
    non_valuable_files_second_round = additional_files_downloaded * fraction_deleted_second_round # eval: 240.0 = 400 * 0.6

    #: L4
    valuable_files_second_round = 150.0 # eval: 150.0 = 150.0

    #: L5
    total_valuable_files = valuable_files_first_round + valuable_files_second_round # eval: 390.0 = 240.0 + 150.0

    #: FA
    answer = total_valuable_files
    return answer # eval: return 390.0
