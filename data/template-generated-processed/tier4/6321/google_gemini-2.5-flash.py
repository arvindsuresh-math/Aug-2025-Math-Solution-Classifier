from fractions import Fraction

def solve():
    """Index: 6321.
    Returns: the total amount Laura paid for all the products.
    """
    # L1
    num_salads = 2 # two salads
    cost_per_salad = 3 # One salad costs $3
    total_cost_salads = num_salads * cost_per_salad

    # L2
    beef_price_multiplier = 2 # two times more expensive
    cost_per_kg_beef = beef_price_multiplier * cost_per_salad

    # L3
    num_kg_beef = 2 # 2 kilograms of beef
    total_cost_beef = num_kg_beef * cost_per_kg_beef

    # L4
    potato_cost_fraction = Fraction(1, 3) # one-third of the price of one salad
    total_cost_potatoes = cost_per_salad * potato_cost_fraction

    # L5
    num_liters_juice = 2 # two liters of juice
    cost_per_liter_juice = 1.5 # one liter of juice is $1.5
    total_cost_juice = num_liters_juice * cost_per_liter_juice

    # L6
    total_cost_all_products = total_cost_salads + total_cost_beef + total_cost_potatoes + total_cost_juice

    # FA
    answer = total_cost_all_products
    return answer