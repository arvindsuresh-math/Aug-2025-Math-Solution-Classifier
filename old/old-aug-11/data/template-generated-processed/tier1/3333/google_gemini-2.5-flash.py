def solve():
    """Index: 3333.
    Returns: the number of days it will take Roberta to listen to her record collection.
    """
    # L1
    initial_records = 8 # 8 vinyl records
    received_records = 12 # 12 records for her birthday
    bought_records = 30 # bought 30 more at a garage sale
    total_records = initial_records + received_records + bought_records

    # L2
    days_per_record = 2 # 2 days to listen to 1 record
    total_days = days_per_record * total_records

    # FA
    answer = total_days
    return answer