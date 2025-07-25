def solve():
    """Index: 4031.
    Returns: the number of strawberries left in each bucket.
    """
    # L1
    total_strawberries = 300 # Cheryl placed 300 strawberries
    num_buckets = 5 # into 5 buckets
    strawberries_per_bucket_initial = total_strawberries / num_buckets

    # L2
    removed_strawberries_per_bucket = 20 # take 20 out of each bucket
    strawberries_per_bucket_final = strawberries_per_bucket_initial - removed_strawberries_per_bucket

    # FA
    answer = strawberries_per_bucket_final
    return answer