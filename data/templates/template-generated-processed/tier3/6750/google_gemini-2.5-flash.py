def solve():
    """Index: 6750.
    Returns: the total number of dishes the restaurant made.
    """
    # L1
    first_shipment_weight = 7 # The first two shipments of 7
    second_shipment_weight = 13 # and 13 pounds
    sum_first_two_shipments = first_shipment_weight + second_shipment_weight

    # L2
    next_day_shipment_weight = 45 # The next day's shipment was 45 pounds of couscous
    total_couscous_weight = sum_first_two_shipments + next_day_shipment_weight

    # L3
    couscous_per_dish = 5 # it takes 5 pounds of couscous to make a dish
    number_of_dishes = total_couscous_weight / couscous_per_dish

    # FA
    answer = number_of_dishes
    return answer