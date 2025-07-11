def solve():
    """Index: 2837.
    Returns: the total amount Leila should pay Ali for the cakes.
    """
    # L1
    price_chocolate = 12 # $12 each (chocolate cakes)
    num_chocolate = 3 # 3 chocolate cakes
    chocolate_total = price_chocolate * num_chocolate

    # L2
    price_strawberry = 22 # $22 each (strawberry cakes)
    num_strawberry = 6 # 6 strawberry cakes
    strawberry_total = price_strawberry * num_strawberry

    # L3
    total_payment = chocolate_total + strawberry_total

    # FA
    answer = total_payment
    return answer