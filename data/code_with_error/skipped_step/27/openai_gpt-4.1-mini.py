def solve(
    initial_files: int = 800,  # After downloading 800 files
    percent_deleted_first_round: float = 70,  # he deleted 70% of them
    second_round_files: int = 400,  # He downloaded 400 more files
    fraction_irrelevant_second_round: float = 3/5  # 3/5 of them were irrelevant
):
    """Index: 27.
    Returns: the number of valuable files Brennan was left with after deleting unrelated files from the second round.
    """

    #: L1
    non_valuable_first_round = (percent_deleted_first_round / 100) * initial_files

    #: L2
    valuable_first_round = initial_files - non_valuable_first_round

    #: L3
    non_valuable_second_round = fraction_irrelevant_second_round * second_round_files

    #: L4
    valuable_second_round = second_round_files - non_valuable_second_round

    #: L5

    #: FA
    answer = percent_deleted_first_round
    return answer