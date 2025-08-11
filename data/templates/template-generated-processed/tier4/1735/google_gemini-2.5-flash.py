def solve():
    """Index: 1735.
    Returns: Karl's total income.
    """
    # L1
    original_tshirt_cost = 5 # T-shirt that costs $5
    refurbished_tshirt_divisor = 2 # half the original price
    refurbished_tshirt_cost = original_tshirt_cost / refurbished_tshirt_divisor

    # L2
    num_refurbished_tshirts_sold = 6 # six refurbished T-shirts
    income_refurbished_tshirts = refurbished_tshirt_cost * num_refurbished_tshirts_sold

    # L3
    num_tshirts_sold = 2 # two T-shirts
    income_tshirts = original_tshirt_cost * num_tshirts_sold

    # L4
    pants_cost = 4 # pants that cost $4
    num_pants_sold = 1 # one pair of pants
    income_pants = pants_cost * num_pants_sold

    # L5
    skirts_cost = 6 # skirts that cost $6
    num_skirts_sold = 4 # four skirts
    income_skirts = skirts_cost * num_skirts_sold

    # L6
    total_income = income_refurbished_tshirts + income_tshirts + income_pants + income_skirts

    # FA
    answer = total_income
    return answer