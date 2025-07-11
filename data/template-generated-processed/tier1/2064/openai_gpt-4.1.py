def solve():
    """Index: 2064.
    Returns: the total price of the purchases in dollars.
    """
    # L1
    refrigerator_price = 4275 # the price of the refrigerator is $4275
    washing_machine_less = 1490 # the price of the washing machine is $1490 less than the price of the refrigerator
    washing_machine_price = refrigerator_price - washing_machine_less

    # L2
    total_price = refrigerator_price + washing_machine_price

    # FA
    answer = total_price
    return answer