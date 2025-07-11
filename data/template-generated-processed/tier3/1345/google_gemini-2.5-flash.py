def solve():
    """Index: 1345.
    Returns: the amount Mimi spent on clothes.
    """
    # L1
    adidas_purchase_cost = 600 # Mimi's Adidas sneakers purchase was $600
    skechers_multiplier = 5 # 1/5 the cost of Skechers
    skechers_cost = skechers_multiplier * adidas_purchase_cost

    # L2
    nike_multiplier = 3 # thrice as much on Nike sneakers
    nike_sneakers_cost = nike_multiplier * adidas_purchase_cost

    # L3
    total_athletic_sneaker_cost = adidas_purchase_cost + nike_sneakers_cost + skechers_cost

    # L4
    total_spent_on_weekend = 8000 # spent $8,000 on athletic sneakers and clothes
    clothes_cost = total_spent_on_weekend - total_athletic_sneaker_cost

    # FA
    answer = clothes_cost
    return answer