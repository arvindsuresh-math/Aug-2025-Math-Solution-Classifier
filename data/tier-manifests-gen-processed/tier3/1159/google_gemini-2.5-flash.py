from fractions import Fraction

def solve():
    """Index: 1159.
    Returns: the total amount Erwan spent after all discounts.
    """
    # L1
    shoe_price = 200 # a pair of shoes at $200
    discount_percentage = Fraction(30, 100) # discounted 30%
    shoe_discount = shoe_price * discount_percentage

    # L2
    shoes_cost_after_discount = shoe_price - shoe_discount

    # L3
    shirt_price_each = 80 # $80 each
    num_shirts = 2 # two shirts
    total_shirts_cost = shirt_price_each * num_shirts

    # L4
    initial_purchase_cost = shoes_cost_after_discount + total_shirts_cost

    # L5
    additional_discount_percentage = Fraction(5, 100) # an additional 5% discount
    additional_discount_amount = initial_purchase_cost * additional_discount_percentage

    # L6
    final_spent_amount = initial_purchase_cost - additional_discount_amount

    # FA
    answer = final_spent_amount
    return answer