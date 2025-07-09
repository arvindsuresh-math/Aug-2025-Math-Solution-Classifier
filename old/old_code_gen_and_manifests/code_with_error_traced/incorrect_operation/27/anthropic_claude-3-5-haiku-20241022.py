def solve(
    first_download_files: int = 800,  # After downloading 800 files
    first_download_delete_percent: float = 0.7,  # he deleted 70% of them
    second_download_files: int = 400,  # He downloaded 400 more files
    second_download_delete_fraction: float = 3/5  # 3/5 of them were irrelevant
):
    """Index: 27.
    Returns: the total number of valuable files Brennan was left with after both download rounds."""

    #: L1
    first_round_non_valuable_files = first_download_files * first_download_delete_percent # eval: 560.0 = 800 * 0.7

    #: L2
    first_round_valuable_files = first_download_files - first_round_non_valuable_files # eval: 240.0 = 800 - 560.0

    #: L3
    second_round_non_valuable_files = second_download_files + second_download_delete_fraction # eval: 400.6 = 400 + 0.6

    #: L4
    second_round_valuable_files = second_download_files - second_round_non_valuable_files # eval: -0.6000000000000227 = 400 - 400.6

    #: L5
    total_valuable_files = first_round_valuable_files + second_round_valuable_files # eval: 239.39999999999998 = 240.0 + -0.6000000000000227

    #: FA
    answer = total_valuable_files
    return answer # eval: return 239.39999999999998
