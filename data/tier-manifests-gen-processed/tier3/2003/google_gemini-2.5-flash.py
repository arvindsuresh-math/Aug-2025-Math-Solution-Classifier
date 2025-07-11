def solve():
    """Index: 2003.
    Returns: the number of bulk boxes of candied yams the store needs to order.
    """
    # L1
    total_shoppers = 375 # 375 predicted holiday shoppers
    shopper_frequency = 3 # Every third shopper
    packages_needed = total_shoppers / shopper_frequency

    # L2
    packages_per_box = 25 # bulk boxes of 25 packages
    bulk_boxes_needed = packages_needed / packages_per_box

    # FA
    answer = bulk_boxes_needed
    return answer