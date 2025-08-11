def solve():
    """Index: 6431.
    Returns: the amount of money that came out of John's pocket.
    """
    # L1
    playstation_value = 400 # The PlayStation was worth $400
    loss_percent = 0.2 # sold it for 20% less
    loss_amount = playstation_value * loss_percent

    # L2
    selling_price = playstation_value - loss_amount

    # L3
    computer_cost = 700 # The computer's cost was $700
    accessories_cost = 200 # the accessories cost was $200
    total_computer_cost = computer_cost + accessories_cost

    # L4
    out_of_pocket_money = total_computer_cost - selling_price

    # FA
    answer = out_of_pocket_money
    return answer