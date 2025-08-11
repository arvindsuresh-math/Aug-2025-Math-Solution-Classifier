def solve():
    """Index: 1086.
    Returns: the number of kilograms of tomatoes not sold.
    """
    # L1
    sold_to_maxwell = 125.5 # sold 125.5 kg to Mrs. Maxwell
    sold_to_wilson = 78 # and 78 kg to Mr. Wilson
    total_sold_tomatoes = sold_to_maxwell + sold_to_wilson

    # L2
    total_harvested_tomatoes = 245.5 # harvested 245.5 kg of tomatoes
    unsold_tomatoes = total_harvested_tomatoes - total_sold_tomatoes

    # FA
    answer = unsold_tomatoes
    return answer