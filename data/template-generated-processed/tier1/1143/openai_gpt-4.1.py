def solve():
    """Index: 1143.
    Returns: the change Kendra received after buying two wooden toys and three hats with a $100 bill.
    """
    # L1
    num_toys = 2 # bought two wooden toys
    toy_price = 20 # price of buying a wooden toy at the new Craftee And Best store is $20
    toys_total = num_toys * toy_price

    # L2
    num_hats = 3 # bought three hats
    hat_price = 10 # cost of buying a hat is $10
    hats_total = num_hats * hat_price

    # L3
    total_cost = toys_total + hats_total

    # L4
    bill = 100 # went to the shop with a $100 bill
    change = bill - total_cost

    # FA
    answer = change
    return answer