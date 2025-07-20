def solve():
    """Index: 5936.
    Returns: the amount of flour Traci brought from her own house in grams.
    """
    # L1
    num_cakes_total = 9 # Traci and Harris have created 9 cakes each (interpreted as 9 cakes total for flour calculation)
    flour_per_cake = 100 # Each cake needs 100g of flour
    total_flour_needed = num_cakes_total * flour_per_cake

    # L2
    harris_flour = 400 # Harris has 400g of flour in his house
    traci_flour_brought = total_flour_needed - harris_flour

    # FA
    answer = traci_flour_brought
    return answer