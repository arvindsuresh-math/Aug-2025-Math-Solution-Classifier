def solve():
    """Index: 3106.
    Returns: the total kilograms of tomatoes Marta had ready for sale on Tuesday.
    """
    # L1
    initial_shipment_friday = 1000 # shipment of 1000 kg of tomatoes arrived
    sold_saturday = 300 # sold a total of 300 kg of tomatoes
    remaining_after_saturday_sale = initial_shipment_friday - sold_saturday

    # L2
    rotted_sunday = 200 # 200 kg of tomatoes to rot
    remaining_after_sunday_rot = remaining_after_saturday_sale - rotted_sunday

    # L3
    multiplier_monday_shipment = 2 # twice the size of the first one
    monday_shipment_size = multiplier_monday_shipment * initial_shipment_friday

    # L4
    total_for_tuesday = remaining_after_sunday_rot + monday_shipment_size

    # FA
    answer = total_for_tuesday
    return answer