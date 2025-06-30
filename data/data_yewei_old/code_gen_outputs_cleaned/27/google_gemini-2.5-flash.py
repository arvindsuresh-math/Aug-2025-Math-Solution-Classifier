def solve():
    # Initial download
    initial_files_downloaded = 800
    percentage_deleted_first_round = 0.70  # 70%

    # Calculate files deleted in the first round
    files_deleted_first_round = initial_files_downloaded * percentage_deleted_first_round
    # Calculate valuable files remaining from the first round
    valuable_files_first_round = initial_files_downloaded - files_deleted_first_round

    # Second download
    second_download_files = 400
    fraction_irrelevant_second_round = 3/5

    # Calculate irrelevant files in the second round
    irrelevant_files_second_round = second_download_files * fraction_irrelevant_second_round
    # Calculate valuable files from the second round
    valuable_files_second_round = second_download_files - irrelevant_files_second_round

    # Total valuable files
    total_valuable_files = valuable_files_first_round + valuable_files_second_round

    return int(total_valuable_files)

# Execute the function to get the answer
# answer = solve()
# print(answer)