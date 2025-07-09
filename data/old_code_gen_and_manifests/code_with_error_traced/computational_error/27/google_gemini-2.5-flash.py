def solve(
        initial_files_downloaded: int = 800, # After downloading 800 files
        percentage_deleted_first_round: float = 0.70, # he deleted 70% of them
        additional_files_downloaded: int = 400, # He downloaded 400 more files
        fraction_irrelevant_second_round: float = 3/5 # 3/5 of them were irrelevant
    ):
    """Index: 27.
    Returns: the number of valuable files Brennan was left with after deleting unrelated files from the second round of downloads.
    """

    #: L1
    non_valuable_first_round = percentage_deleted_first_round * initial_files_downloaded # eval: 560.0 = 0.7 * 800

    #: L2
    valuable_first_round = initial_files_downloaded - non_valuable_first_round # eval: 240.0 = 800 - 560.0

    #: L3
    non_useful_second_round = fraction_irrelevant_second_round * additional_files_downloaded # eval: 240.0 = 0.6 * 400

    #: L4
    valuable_second_round = additional_files_downloaded - non_useful_second_round # eval: 160.0 = 400 - 240.0

    #: L5
    total_valuable_files = 410.0 # eval: 410.0 = 410.0

    #: FA
    answer = total_valuable_files
    return answer # eval: return 410.0
