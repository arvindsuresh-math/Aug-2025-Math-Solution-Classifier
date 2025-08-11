def solve():
    """Index: 787.
    Returns: the total pounds of sand collected by Eden, Mary, and Iris.
    """
    # L1
    eden_buckets = 4 # Eden carried 4 buckets of sand
    mary_more_than_eden = 3 # Mary carried 3 more buckets of sand than Eden
    mary_buckets = eden_buckets + mary_more_than_eden

    # L2
    iris_less_than_mary = 1 # Iris carried 1 less bucket of sand than Mary
    iris_buckets = mary_buckets - iris_less_than_mary

    # L3
    total_buckets = eden_buckets + mary_buckets + iris_buckets

    # L4
    pounds_per_bucket = 2 # each bucket contains 2 pounds of sand
    total_pounds = total_buckets * pounds_per_bucket

    # FA
    answer = total_pounds
    return answer