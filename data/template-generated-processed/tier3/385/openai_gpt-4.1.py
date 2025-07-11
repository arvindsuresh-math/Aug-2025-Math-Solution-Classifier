def solve():
    """Index: 385.
    Returns: the total number of pounds of strawberries picked by Sally, Jenny, and Moses.
    """
    # L1
    entrance_fee_per_person = 4 # Miguel charges each interested picker $4
    number_of_pickers = 3 # Sally, Jenny and Moses
    total_entrance_fee = entrance_fee_per_person * number_of_pickers

    # L2
    total_paid = 128 # They paid $128 for their harvest
    pre_discount_cost = total_paid + total_entrance_fee

    # L3
    price_per_pound = 20 # the standard price of a pound of strawberries is $20
    total_pounds = pre_discount_cost / price_per_pound

    # FA
    answer = total_pounds
    return answer