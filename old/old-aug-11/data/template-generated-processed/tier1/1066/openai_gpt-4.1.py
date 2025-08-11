def solve():
    """Index: 1066.
    Returns: the total number of fruits George and Amelia pick altogether.
    """
    # L1
    george_oranges = 45 # George picks 45 oranges
    amelia_oranges_less = 18 # Amelia picks 18 fewer oranges than George
    amelia_oranges = george_oranges - amelia_oranges_less

    # L2
    total_oranges = george_oranges + amelia_oranges

    # L3
    amelia_apples = 15 # Amelia picks 15 apples
    george_apples_more = 5 # George picks 5 more apples than Amelia
    george_apples = amelia_apples + george_apples_more

    # L4
    total_apples = george_apples + amelia_apples

    # L5
    answer = total_oranges + total_apples
    return answer