def solve():
    """Index: 5267.
    Returns: the total amount of money James spent.
    """
    # L1
    milk_cost = 3 # a gallon of milk for $3
    bananas_cost = 2 # a bunch of bananas for $2
    subtotal_purchases = milk_cost + bananas_cost

    # L2
    sales_tax_rate = 0.2 # paid 20% sales tax
    sales_tax_amount = subtotal_purchases * sales_tax_rate

    # L3
    total_spent = subtotal_purchases + sales_tax_amount

    # FA
    answer = total_spent
    return answer