def solve():
    """Index: 3639.
    Returns: the number of pizza slices left over.
    """
    # L1
    num_small_pizzas = 3 # George purchased 3 small
    slices_per_small_pizza = 4 # A small pizza can gives 4 slices
    slices_from_small_pizzas = num_small_pizzas * slices_per_small_pizza

    # L2
    num_large_pizzas = 2 # and 2 large pizzas
    slices_per_large_pizza = 8 # a large pizza gives 8 slices
    slices_from_large_pizzas = num_large_pizzas * slices_per_large_pizza

    # L3
    total_george_slices = slices_from_small_pizzas + slices_from_large_pizzas

    # L4
    george_eats = 3 # George would like to eat 3 pieces
    bob_extra_slices = 1 # one more piece than George
    bob_eats = george_eats + bob_extra_slices

    # L5
    susie_fraction_numerator = 1 # half as many as Bob
    susie_fraction_denominator = 2 # half as many as Bob
    susie_eats = susie_fraction_numerator / susie_fraction_denominator * bob_eats

    # L6
    bill_eats = 3 # Bill, Fred and Mark would each like 3 pieces
    fred_eats = 3 # Bill, Fred and Mark would each like 3 pieces
    mark_eats = 3 # Bill, Fred and Mark would each like 3 pieces
    bill_fred_mark_eats = bill_eats + fred_eats + mark_eats

    # L7
    total_eaten_slices = george_eats + bob_eats + susie_eats + bill_fred_mark_eats

    # L8
    remaining_slices = total_george_slices - total_eaten_slices

    # FA
    answer = remaining_slices
    return answer