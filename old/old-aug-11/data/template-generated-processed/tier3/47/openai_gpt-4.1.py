def solve():
    """Index: 47.
    Returns: the total time in seconds to download the entire file.
    """
    # L1
    first_chunk_size = 60 # first 60 megabytes
    first_chunk_rate = 5 # 5 megabytes per second
    first_chunk_time = first_chunk_size / first_chunk_rate

    # L2
    total_file_size = 90 # 90 megabytes in size
    remaining_chunk_size = total_file_size - first_chunk_size

    # L3
    remaining_chunk_rate = 10 # 10 megabytes per second thereafter
    remaining_chunk_time = remaining_chunk_size / remaining_chunk_rate

    # L4
    answer = first_chunk_time + remaining_chunk_time
    return answer