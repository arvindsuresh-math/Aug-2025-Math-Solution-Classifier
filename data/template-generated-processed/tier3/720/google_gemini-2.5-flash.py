from fractions import Fraction

def solve():
    """Index: 720.
    Returns: the total loss Mr. Callen made from the sale of the items.
    """
    # L1
    painting_loss_percentage = Fraction(10, 100) # 10% less
    painting_cost = 40 # $40 each
    loss_per_painting = painting_loss_percentage * painting_cost

    # L2
    num_paintings = 10 # 10 paintings
    total_loss_paintings = num_paintings * loss_per_painting

    # L3
    toy_loss_percentage = Fraction(15, 100) # 15% less
    toy_cost = 20 # $20 each
    loss_per_toy = toy_loss_percentage * toy_cost

    # L4
    num_toys = 8 # 8 wooden toys
    total_loss_toys = loss_per_toy * num_toys

    # L5
    total_loss = total_loss_paintings + total_loss_toys

    # FA
    answer = total_loss
    return answer