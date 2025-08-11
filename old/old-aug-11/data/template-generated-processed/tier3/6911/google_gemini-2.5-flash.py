def solve():
    """Index: 6911.
    Returns: the number of tubs the pharmacy will buy from the usual vendor.
    """
    # L1
    total_needed_tubs = 100 # a total of 100 tubs for the week
    tubs_in_storage = 20 # 20 tubs left in storage
    tubs_still_needed = total_needed_tubs - tubs_in_storage

    # L2
    new_vendor_divisor = 4 # a quarter from a new vendor
    tubs_from_new_vendor = tubs_still_needed / new_vendor_divisor

    # L3
    tubs_after_new_vendor_purchase = tubs_in_storage + tubs_from_new_vendor

    # L4
    tubs_from_usual_vendor = total_needed_tubs - tubs_after_new_vendor_purchase

    # FA
    answer = tubs_from_usual_vendor
    return answer