def solve():
    """Index: 4487.
    Returns: the total number of calories Jean eats.
    """
    # L1
    total_pages_written = 12 # 12 pages
    pages_per_donut = 2 # 2 pages
    total_donuts = total_pages_written / pages_per_donut

    # L2
    calories_per_donut = 150 # 150 calories
    total_calories = total_donuts * calories_per_donut

    # FA
    answer = total_calories
    return answer