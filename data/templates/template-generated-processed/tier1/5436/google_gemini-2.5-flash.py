def solve():
    """Index: 5436.
    Returns: the total time it takes to put on her full face.
    """
    # L1
    num_facial_products = 5 # 5 facial products
    minutes_per_product_application = 5 # waits 5 minutes between each product
    time_for_products = num_facial_products * minutes_per_product_application

    # L2
    additional_makeup_time = 30 # an additional 30 minutes putting on her make-up
    total_time = time_for_products + additional_makeup_time

    # FA
    answer = total_time
    return answer