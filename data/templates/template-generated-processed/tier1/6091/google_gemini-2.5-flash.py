def solve():
    """Index: 6091.
    Returns: the number of customers who tried a sample.
    """
    # L1
    products_per_box = 20 # boxes of 20
    boxes_opened = 12 # open 12 boxes
    total_samples_put_out = products_per_box * boxes_opened

    # L2
    samples_left_over = 5 # five samples left over
    samples_used = total_samples_put_out - samples_left_over

    # L3
    samples_per_customer = 1 # limited to one per person
    customers_tried_sample = samples_used * samples_per_customer

    # FA
    answer = customers_tried_sample
    return answer