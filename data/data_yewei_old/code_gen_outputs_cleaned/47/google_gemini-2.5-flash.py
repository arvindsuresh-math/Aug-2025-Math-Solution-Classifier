def solve():
    # Total file size in megabytes
    total_file_size_mb = 90
    
    # First part of the download
    first_part_size_mb = 60
    first_part_speed_mbps = 5
    
    # Calculate time for the first part
    time_first_part_seconds = first_part_size_mb / first_part_speed_mbps
    
    # Remaining part of the download
    remaining_size_mb = total_file_size_mb - first_part_size_mb
    remaining_part_speed_mbps = 10
    
    # Calculate time for the remaining part
    time_remaining_part_seconds = remaining_size_mb / remaining_part_speed_mbps
    
    # Calculate total download time
    total_download_time_seconds = time_first_part_seconds + time_remaining_part_seconds
    
    return total_download_time_seconds

# Execute the function to get the answer
answer = solve()