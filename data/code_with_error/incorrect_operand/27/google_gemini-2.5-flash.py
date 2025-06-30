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
    non_valuable_first_round = percentage_deleted_first_round * initial_files_downloaded

    #: L2
    valuable_first_round = additional_files_downloaded - non_valuable_first_round

    #: L3
    non_useful_second_round = fraction_irrelevant_second_round * additional_files_downloaded

    #: L4
    valuable_second_round = additional_files_downloaded - non_useful_second_round

    #: L5
    total_valuable_files = valuable_second_round + valuable_first_round

    #: FA
    answer = total_valuable_files
    return answer