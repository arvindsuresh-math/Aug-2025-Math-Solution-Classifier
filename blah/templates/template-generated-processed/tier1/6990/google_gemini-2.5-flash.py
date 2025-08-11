def solve():
    """Index: 6990.
    Returns: the total pounds of flour Sarah has.
    """
    # L1
    rye_flour_bought = 5 # 5 pounds of rye flour
    whole_wheat_bread_flour_bought = 10 # 10 pounds of whole-wheat bread flour
    chickpea_flour_bought = 3 # 3 pounds of chickpea flour
    total_bought_flour = rye_flour_bought + whole_wheat_bread_flour_bought + chickpea_flour_bought

    # L2
    whole_wheat_pastry_flour_had = 2 # 2 pounds of whole-wheat pastry flour
    total_flour_now = total_bought_flour + whole_wheat_pastry_flour_had

    # FA
    answer = total_flour_now
    return answer