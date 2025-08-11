def solve():
    """Index: 3701.
    Returns: the total number of sneezes.
    """
    # L1
    sneezing_duration_minutes = 2 # 2 minutes
    seconds_per_minute = 60 # WK
    total_sneezing_seconds = sneezing_duration_minutes * seconds_per_minute

    # L2
    sneeze_interval_seconds = 3 # once every 3 seconds
    total_sneezes = total_sneezing_seconds / sneeze_interval_seconds

    # FA
    answer = total_sneezes
    return answer