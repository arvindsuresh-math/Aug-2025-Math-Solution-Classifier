from fractions import Fraction

def solve():
    """Index: 3440.
    Returns: the total amount of money Mica should have.
    """
    # L1
    pasta_kg = 2 # 2 kilograms of pasta
    pasta_cost_per_kg = 1.5 # $1.5
    total_pasta_cost = pasta_cost_per_kg * pasta_kg

    # L2
    beef_cost_per_kg = 8 # $8 for 1 kilogram
    beef_kg_fraction = Fraction(1, 4) # 1/4 kilogram of ground beef
    total_beef_cost = beef_cost_per_kg * beef_kg_fraction

    # L3
    sauce_jars = 2 # two jars of pasta sauce
    sauce_cost_per_jar = 2 # $2 per jar
    total_sauce_cost = sauce_cost_per_jar * sauce_jars

    # L4
    cost_food_items = total_pasta_cost + total_beef_cost + total_sauce_cost

    # L5
    quesadilla_cost = 6 # a $6 Quesadilla
    total_money_needed = cost_food_items + quesadilla_cost

    # FA
    answer = total_money_needed
    return answer