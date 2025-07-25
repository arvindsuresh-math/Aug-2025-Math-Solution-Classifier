def solve():
    """Index: 3634.
    Returns: the amount Haily would spend at the cheapest salon.
    """
    # L1
    gustran_haircut_price = 45 # haircut is $45
    gustran_facial_price = 22 # facial cleaning is $22
    gustran_nails_price = 30 # nails are $30
    gustran_total_price = gustran_haircut_price + gustran_facial_price + gustran_nails_price

    # L2
    barbara_nails_price = 40 # nails are $40
    barbara_haircut_price = 30 # haircut is $30
    barbara_facial_price = 28 # facial cleaning is $28
    barbara_total_price = barbara_nails_price + barbara_haircut_price + barbara_facial_price

    # L3
    fancy_facial_price = 30 # facial cleaning is $30
    fancy_haircut_price = 34 # haircut is $34
    fancy_nails_price = 20 # nails are $20
    fancy_total_price = fancy_facial_price + fancy_haircut_price + fancy_nails_price

    # L4
    cheapest_price = min(gustran_total_price, barbara_total_price, fancy_total_price)

    # FA
    answer = cheapest_price
    return answer