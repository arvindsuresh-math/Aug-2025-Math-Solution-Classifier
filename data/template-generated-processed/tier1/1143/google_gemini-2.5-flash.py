def solve():
    """Index: 1143.
    Returns: the change Kendra received.
    """
    # L1
    num_toys_bought = 2 # bought two wooden toys
    price_toy = 20 # The price of buying a wooden toy ... is $20
    cost_toys = num_toys_bought * price_toy

    # L2
    num_hats_bought = 3 # and three hats
    price_hat = 10 # the cost of buying a hat is $10
    cost_hats = num_hats_bought * price_hat

    # L3
    total_cost = cost_toys + cost_hats

    # L4
    bill_amount = 100 # with a $100 bill
    change_received = bill_amount - total_cost

    # FA
    answer = change_received
    return answer