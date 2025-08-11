from fractions import Fraction

def solve():
    """Index: 5728.
    Returns: the total cost of 2 slices of cake and 1 cup of milk tea.
    """
    # L1
    milk_tea_cost = 2.40 # If the milk tea costs $2.40
    cake_cost_fraction = Fraction(3, 4) # three-fourths of the cost of a cup of milk tea
    slice_cake_cost = milk_tea_cost * cake_cost_fraction

    # L2
    num_cake_slices = 2 # 2 slices of cake
    two_slices_cake_cost = slice_cake_cost * num_cake_slices

    # L3
    total_cost = two_slices_cake_cost + milk_tea_cost

    # FA
    answer = total_cost
    return answer