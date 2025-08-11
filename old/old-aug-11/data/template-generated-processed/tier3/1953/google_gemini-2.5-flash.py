from fractions import Fraction

def solve():
    """Index: 1953.
    Returns: the total amount the school paid for the models.
    """
    # L1
    kindergarten_models = 2 # bought 2 models for the kindergarten library
    elementary_multiplier = 2 # twice as many for the elementary library
    elementary_models = kindergarten_models * elementary_multiplier

    # L2
    total_models = kindergarten_models + elementary_models

    # L3
    original_price_per_model = 100 # dinosaur models for $100 each
    discount_percentage = Fraction(5, 100) # 5% reduction in price
    discount_amount = original_price_per_model * discount_percentage

    # L4
    final_model_cost = original_price_per_model - discount_amount

    # L5
    total_paid = final_model_cost * total_models

    # FA
    answer = total_paid
    return answer