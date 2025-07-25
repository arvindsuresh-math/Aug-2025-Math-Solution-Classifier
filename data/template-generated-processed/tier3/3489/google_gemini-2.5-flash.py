def solve():
    """Index: 3489.
    Returns: the number of times Enrique will shred paper.
    """
    # L1
    num_contracts = 2 # 2 contracts
    pages_per_contract = 132 # 132 pages each
    total_pages = num_contracts * pages_per_contract

    # L2
    shredder_capacity = 6 # shred 6 pages at a time
    shredding_times = total_pages / shredder_capacity

    # FA
    answer = shredding_times
    return answer