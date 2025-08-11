def solve():
    """Index: 3146.
    Returns: the number of rounds it will take to fill the pool.
    """
    # L1
    george_buckets_per_round = 2 # George can carry two buckets each round
    harry_buckets_per_round = 3 # Harry can carry three buckets each round
    buckets_per_round = george_buckets_per_round + harry_buckets_per_round

    # L2
    total_buckets_needed = 110 # 110 buckets to fill the pool
    total_rounds = total_buckets_needed / buckets_per_round

    # FA
    answer = total_rounds
    return answer