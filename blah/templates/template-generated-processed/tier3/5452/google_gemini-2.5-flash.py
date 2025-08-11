from fractions import Fraction

def solve():
    """Index: 5452.
    Returns: Esperanza's gross monthly salary.
    """
    # L1
    food_fraction = Fraction(3, 5) # 3/5 as much money on food
    rent_cost = 600 # $600 in rent
    food_cost = food_fraction * rent_cost

    # L2
    mortgage_multiplier = 3 # three times the amount of money she spends on food
    mortgage_cost = mortgage_multiplier * food_cost

    # L3
    tax_fraction = Fraction(2, 5) # 2/5 of her savings in taxes
    savings = 2000 # saves $2000
    tax_cost = tax_fraction * savings

    # L4
    total_expenses = tax_cost + mortgage_cost + food_cost + rent_cost

    # L5
    gross_salary = total_expenses + savings

    # FA
    answer = gross_salary
    return answer