from fractions import Fraction

def solve():
    """Index: 27.
    Returns: the total number of valuable files Brennan was left with.
    """
    # L1
    deleted_percentage_first_round = Fraction(70, 100) # deleted 70% of them
    initial_download_files = 800 # downloading 800 files
    non_valuable_files_first_round = deleted_percentage_first_round * initial_download_files

    # L2
    valuable_files_first_round = initial_download_files - non_valuable_files_first_round

    # L3
    second_download_files = 400 # downloaded 400 more files
    irrelevant_fraction_second_round = Fraction(3, 5) # 3/5 of them were irrelevant
    non_useful_files_second_round = irrelevant_fraction_second_round * second_download_files

    # L4
    valuable_files_second_round = second_download_files - non_useful_files_second_round

    # L5
    total_valuable_files = valuable_files_second_round + valuable_files_first_round

    # FA
    answer = total_valuable_files
    return answer