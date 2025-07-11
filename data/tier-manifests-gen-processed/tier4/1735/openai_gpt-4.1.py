def solve():
    """Index: 1735.
    Returns: Karl's total income from all clothing sales.
    """
    # L1
    tshirt_price = 5 # T-shirt that costs $5
    refurb_divisor = 2 # half the original price
    refurb_tshirt_price = tshirt_price / refurb_divisor

    # L2
    refurb_tshirt_sold = 6 # six refurbished T-shirts
    refurb_tshirt_income = refurb_tshirt_price * refurb_tshirt_sold

    # L3
    tshirt_sold = 2 # two T-shirts
    tshirt_income = tshirt_price * tshirt_sold

    # L4
    pants_price = 4 # pants that cost $4
    pants_sold = 1 # one pair of pants
    pants_income = pants_price * pants_sold

    # L5
    skirt_price = 6 # skirts that cost $6
    skirt_sold = 4 # four skirts
    skirt_income = skirt_price * skirt_sold

    # L6
    total_income = refurb_tshirt_income + tshirt_income + pants_income + skirt_income

    # FA
    answer = total_income
    return answer