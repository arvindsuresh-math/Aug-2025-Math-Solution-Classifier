def solve(
    initial_files_downloaded: int = 800, # After downloading 800 files
    percentage_deleted_initial: float = 0.7, # he deleted 70% of them
    additional_files_downloaded: int = 400, # He downloaded 400 more files
    fraction_deleted_additional: float = 3/5 # 3/5 of them were irrelevant
):
    """Index: 27.
    Returns: the number of valuable files Brennan was left with.
    """
    #: L1
    non_valuable_initial = initial_files_downloaded * percentage_deleted_initial

    #: L2
    valuable_initial = initial_files_downloaded - non_valuable_initial

    #: L3
    non_valuable_additional = additional_files_downloaded * fraction_deleted_additional

    #: L4
    valuable_additional = additional_files_downloaded - non_valuable_additional

    #: L5
    total_valuable_files = valuable_initial + valuable_additional

    answer = total_valuable_files # FINAL ANSWER
    return answer