def solve():
    """Index: 4179.
    Returns: the number of free gigabytes the new external drive will have.
    """
    # L1
    initial_used_gb = 12.6 # 12.6 gigabytes used
    deleted_folder_gb = 4.6 # delete a folder of size 4.6 gigabytes
    used_after_delete_gb = initial_used_gb - deleted_folder_gb

    # L2
    new_files_gb = 2 # new files of 2 gigabytes
    final_used_gb = used_after_delete_gb + new_files_gb

    # L3
    new_drive_capacity_gb = 20 # new external drive of size 20 gigabytes
    free_space_new_drive_gb = new_drive_capacity_gb - final_used_gb

    # FA
    answer = free_space_new_drive_gb
    return answer