def solve():
    """Index: 4339.
    Returns: the percentage of the initial cost lost.
    """
    # L1
    initial_cost = 300 # smartphone for $300
    sold_price = 255 # sold it for $255
    loss_amount = initial_cost - sold_price

    # L2
    percentage_factor = 100 # WK
    percentage_loss = (loss_amount / initial_cost) * percentage_factor

    # FA
    answer = percentage_loss
    return answer