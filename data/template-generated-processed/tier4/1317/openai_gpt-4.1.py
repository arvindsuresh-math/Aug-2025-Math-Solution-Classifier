def solve():
    """Index: 1317.
    Returns: the average time in seconds for the racers.
    """
    # L1
    diego_half_block_time = 2.5 # Diego runs around half the block in 2.5 minutes
    diego_full_block_multiplier = 2 # to get full block time from half block
    diego_full_block_time = diego_half_block_time * diego_full_block_multiplier

    # L2
    carlos_full_block_time = 3 # Carlos runs around the entire block in 3 minutes
    total_time = carlos_full_block_time + diego_full_block_time

    # L3
    num_racers = 2 # Carlos and Diego
    average_time_minutes = total_time / num_racers

    # L4
    seconds_per_minute = 60 # WK
    average_time_seconds = average_time_minutes * seconds_per_minute

    # FA
    answer = average_time_seconds
    return answer