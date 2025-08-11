from fractions import Fraction

def solve():
    """Index: 4804.
    Returns: the total amount Isabela spent to buy the items.
    """
    # L1
    cucumbers_bought = 100 # bought 100 cucumbers
    cucumbers_to_pencils_ratio = 2 # twice as many cucumbers as pencils
    pencils_bought = cucumbers_bought / cucumbers_to_pencils_ratio

    # L2
    cost_per_item = 20 # costing $20 each
    pencils_cost_no_discount = pencils_bought * cost_per_item

    # L3
    discount_percentage = Fraction(20, 100) # 20% discount
    discount_amount = discount_percentage * pencils_cost_no_discount

    # L4
    pencils_cost_with_discount = pencils_cost_no_discount - discount_amount

    # L5
    cucumbers_total_cost = cost_per_item * cucumbers_bought

    # L6
    total_cost = cucumbers_total_cost + pencils_cost_with_discount

    # FA
    answer = total_cost
    return answer