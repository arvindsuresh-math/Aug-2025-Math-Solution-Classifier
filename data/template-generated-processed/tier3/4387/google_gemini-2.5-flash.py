def solve():
    """Index: 4387.
    Returns: the number of songs Jeff can store on his phone.
    """
    # L1
    total_storage_gb = 16 # 16 GB of storage
    used_storage_gb = 4 # using 4 GB
    remaining_storage_gb = total_storage_gb - used_storage_gb

    # L2
    mb_per_gb = 1000 # There are 1000 MB in a GB
    remaining_storage_mb = remaining_storage_gb * mb_per_gb

    # L3
    song_size_mb = 30 # a song takes up about 30MB
    num_songs = remaining_storage_mb / song_size_mb

    # FA
    answer = num_songs
    return answer