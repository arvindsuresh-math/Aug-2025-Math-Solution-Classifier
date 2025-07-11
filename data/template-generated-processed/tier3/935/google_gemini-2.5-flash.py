def solve():
    """Index: 935.
    Returns: the number of loaves of bread Jim can bake.
    """
    # L1
    flour_cupboard = 200 # 200g of flour in the cupboard
    flour_counter = 100 # 100g of flour on the kitchen counter
    flour_pantry = 100 # 100g in the pantry
    total_flour = flour_cupboard + flour_counter + flour_pantry

    # L2
    flour_per_loaf = 200 # one loaf of bread requires 200g of flour
    num_loaves = total_flour / flour_per_loaf

    # FA
    answer = num_loaves
    return answer