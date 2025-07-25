def solve():
    """Index: 3965.
    Returns: the total number of bags of fruit Austin picked.
    """
    # L1
    dallas_apples = 14 # Dallas picked 14 bags of apples
    austin_more_apples = 6 # 6 bags of apples more than Dallas
    austin_apples = dallas_apples + austin_more_apples

    # L2
    dallas_pears = 9 # 9 bags of pears
    austin_fewer_pears = 5 # 5 fewer bags of pears than Dallas
    austin_pears = dallas_pears - austin_fewer_pears

    # L3
    total_austin_fruit = austin_apples + austin_pears

    # FA
    answer = total_austin_fruit
    return answer