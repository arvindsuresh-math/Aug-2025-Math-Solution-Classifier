def solve():
    """Index: 7070.
    Returns: the total number of pieces of bread needed for the sandwiches.
    """
    # L1
    bread_per_regular_sandwich = 2 # Two pieces of bread are needed for one regular sandwich
    num_regular_sandwiches = 14 # 14 regular sandwiches
    total_bread_regular = bread_per_regular_sandwich * num_regular_sandwiches

    # L2
    bread_per_double_meat_sandwich = 3 # 3 pieces of bread are needed for a double meat sandwich
    num_double_meat_sandwiches = 12 # 12 double meat sandwiches
    total_bread_double_meat = bread_per_double_meat_sandwich * num_double_meat_sandwiches

    # L3
    total_bread_needed = total_bread_regular + total_bread_double_meat

    # FA
    answer = total_bread_needed
    return answer