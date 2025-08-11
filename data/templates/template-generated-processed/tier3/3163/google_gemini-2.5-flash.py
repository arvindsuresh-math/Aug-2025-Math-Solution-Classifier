from fractions import Fraction

def solve():
    """Index: 3163.
    Returns: the number of students in the class.
    """
    # L1
    cheese_ratio_numerator = 2 # 2 pieces of cheese
    onion_ratio_denominator = 1 # 1 piece of onion
    cheese_pizza_ratio = Fraction(cheese_ratio_numerator, cheese_ratio_numerator + onion_ratio_denominator)

    # L2
    total_pizzas = 6 # She orders 6 total pizzas
    num_cheese_pizzas = total_pizzas * cheese_pizza_ratio

    # L3
    slices_per_pizza = 18 # A large pizza has 18 slices
    total_cheese_slices = num_cheese_pizzas * slices_per_pizza

    # L4
    leftover_cheese_slices = 8 # 8 pieces of cheese
    eaten_cheese_slices = total_cheese_slices - leftover_cheese_slices

    # L5
    cheese_slices_per_student = 2 # 2 pieces of cheese
    num_students = eaten_cheese_slices / cheese_slices_per_student

    # FA
    answer = num_students
    return answer