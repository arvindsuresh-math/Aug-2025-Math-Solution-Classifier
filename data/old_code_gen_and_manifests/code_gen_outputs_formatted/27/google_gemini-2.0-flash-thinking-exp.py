def solve(
    initial_files: int = 800, # After downloading 800 files
    initial_irrelevant_percentage: float = 0.70, # he deleted 70% of them
    second_download_files: int = 400, # He downloaded 400 more files
    second_irrelevant_fraction: float = 3/5 # 3/5 of them were irrelevant
):
    """Index: 27.
    Returns: the number of valuable files remaining after the second round of deletions.
    """

    #: L1
    non_valuable_initial = initial_irrelevant_percentage * initial_files

    #: L2
    valuable_initial = initial_files - non_valuable_initial

    #: L3
    non_useful_second = second_irrelevant_fraction * second_download_files

    #: L4
    valuable_second = second_download_files - non_useful_second

    #: L5
    total_valuable_files = valuable_second + valuable_initial

    #: FA
    answer = total_valuable_files
    return answer